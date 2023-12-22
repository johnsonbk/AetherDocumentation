#!/opt/local/bin/python
from __future__ import print_function

import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from math import pi

# filepath = '../outputs/output.Sphere.2members/3DALL_20110320_000000_m0000.nc'

filepath = '../restarts/twenty_member/'

file_prefix = 'neutrals_m'
nmembers = 20
members = [str(member).zfill(4) for member in range(0, nmembers)]

nblocks = 4
blocks = [str(block).zfill(4) for block in range(0, nblocks)]
ntruncate = 2
radians_to_degrees = 180.0/pi

ntimes = 1

#  GGGG RRRR  IIIII DDDD
# G     R   R   I   D   D
# G  GG RRRR    I   D   D
# G   G R  R    I   D   D
#  GGGG R   R IIIII DDDD

# The grid is split among four block files

# Altitudes
# The full range of altitudes can be gathered from any of the block files, so use 0000
grid_filename_0000 = filepath + 'grid_g' + blocks[0] + '.nc'
print('Reading grid file', grid_filename_0000)
grid_file_0000 = netCDF4.Dataset(grid_filename_0000)
nzs = len(grid_file_0000.dimensions['z'])

zs = np.empty(nzs)
zs_0000 = grid_file_0000.variables['Altitude']
zs[:] = zs_0000[0, 0, :]

# Longitudes
# The full range of longitudes can be gathered from files 0000 and 0001
grid_filename_0001 = filepath + 'grid_g' + blocks[1] + '.nc'
print('Reading grid file', grid_filename_0001)
grid_file_0001 = netCDF4.Dataset(grid_filename_0001)
nlons_in_block = len(grid_file_0001.dimensions['x'])
nlons = int(nlons_in_block*nblocks/2-2*ntruncate*nblocks/2)

lons = np.empty(nlons)
lons_0000 = grid_file_0000.variables['Longitude']
lons[0:nlons_in_block-2*ntruncate] = lons_0000[ntruncate:-ntruncate, 0, 0]*radians_to_degrees
lons_0001 = grid_file_0001.variables['Longitude']
lons[nlons_in_block-2*ntruncate:] = lons_0001[ntruncate:-ntruncate, 0, 0]*radians_to_degrees

# Latitudes
# The full range of latitudes can be gathered from files 0000 and 0002
grid_filename_0002 = filepath + 'grid_g' + blocks[2] + '.nc'
print('Reading grid file', grid_filename_0001)
grid_file_0002 = netCDF4.Dataset(grid_filename_0002)
nlats_in_block = len(grid_file_0002.dimensions['y'])
nlats = int(nlats_in_block*nblocks/2-2*ntruncate*nblocks/2)

lats = np.empty(nlats)
lats_0000 = grid_file_0000.variables['Latitude']
lats[0:nlats_in_block-2*ntruncate] = lats_0000[0, ntruncate:-ntruncate, 0]*radians_to_degrees
lats_0002 = grid_file_0002.variables['Latitude']
lats[nlats_in_block-2*ntruncate:] = lats_0002[0, ntruncate:-ntruncate, 0]*radians_to_degrees

grid_file_0000.close()
grid_file_0001.close()
grid_file_0002.close()

for member in members:
    print('member', member)

    # OOOOO U   U TTTTT PPPP  U   U TTTTT
    # O   O U   U   T   P   P U   U   T
    # O   O U   U   T   PPPP  U   U   T
    # O   O U   U   T   P     U   U   T
    # OOOOO UUUUU   T   P      UUU    T

    output_filename = filepath + file_prefix + member + '.nc'
    # print('Creating stitched output file', output_filename)
    output_file = netCDF4.Dataset(output_filename, mode='w')

    # Write dimensions to the output file
    time_dim = output_file.createDimension('time', None)
    z_dim = output_file.createDimension('z', nzs)
    lat_dim = output_file.createDimension('lat', nlats)
    lon_dim = output_file.createDimension('lon', nlons)

    # Write time variable to output file
    time = output_file.createVariable('time', np.int32, ('time',))
    time.units = 'seconds since 1965-01-01 0 UTC'
    time.long_name = 'model time'

    # BKJ 12-21-2023 This is a kludge because the time value is incorrectly set to
    # zero in the input netCDF file.
    time[:] = [1458432000]

    output_field = output_file.createVariable('z', np.float32, ('z'))
    output_field.units = 'meters'
    output_field.long_name = 'Altitude'
    output_field[:] = zs[:]

    output_field = output_file.createVariable('lat', np.float32, ('lat'))
    output_field.units = 'degrees' # input_field.units
    output_field.long_name = 'Latitude'
    output_field[:] = lats[:]

    output_field = output_file.createVariable('lon', np.float32, ('lon'))
    output_field.units = 'degrees' # input_field.units
    output_field.long_name = 'Longitude'
    output_field[:] = lons[:]

    # TTTTT EEEEE M   M PPPP  L       A   TTTTT EEEEEE
    #   T   E     MM MM P   P L      A A    T   E
    #   T   EEEE  M M M PPPP  L     AAAAA   T   EEEEE
    #   T   E     M   M P     L     A   A   T   E
    #   T   EEEEE M   M P     LLLLL A   A   T   EEEEEE

    # The template file gives us the list of variables
    template_input_filename = filepath + file_prefix + member + '_g' + blocks[0] + '.nc'
    print('Reading block file', template_input_filename)
    template_input_file = netCDF4.Dataset(template_input_filename, 'r')

    nvars = len(template_input_file.variables)
    stitched_array = np.empty((nvars, ntimes, nzs, nlons, nlats))

    for ikey, this_key in enumerate(template_input_file.variables):
        if this_key == 'time':
            pass
        else:
            formatted_key = this_key.lower().strip('\\').replace(' ', '_').replace('+','p').replace('-','n')
        
            for iblock, block in enumerate(blocks):
            
                input_filename = filepath + file_prefix + member + '_g' + block + '.nc'
                input_file = netCDF4.Dataset(input_filename, 'r')
                input_field = input_file.variables[this_key]

                # Loop through the z levels so that the array can be reordered from lon, lat, z to z, lat, lon

                for iz in range (0, nzs):

                    if iblock == 0:
                        stitched_array[ikey, 0, iz, 0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate] = np.transpose(input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz])
                    elif iblock == 2:
                        stitched_array[ikey, 0, iz, nlons_in_block-2*ntruncate:, 0:nlats_in_block-2*ntruncate] = np.transpose(input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz])
                    elif iblock == 1:
                        stitched_array[ikey, 0, iz, 0:nlons_in_block-2*ntruncate, nlats_in_block-2*ntruncate:] = np.transpose(input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz])
                    elif iblock == 3:
                        stitched_array[ikey, 0, iz, nlons_in_block-2*ntruncate:, nlats_in_block-2*ntruncate:] = np.transpose(input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz])
                
                input_file.close()
                
            output_field = output_file.createVariable(formatted_key, np.double, ('time', 'z', 'lat', 'lon'))
            # output_field.units = input_field.units
            # output_field.long_name = input_field.long_name
            output_field[:] = stitched_array[ikey, :, :, :, :]

            if formatted_key == 'temperature':

                plt.title('Temperature at highest altitude')
                plt.pcolor(np.transpose(stitched_array[ikey, 0, -1, :, :]), vmin=stitched_array[ikey, 0, -1, :, :].min(), vmax=stitched_array[ikey, 0, -1, :, :].max())
                plt.colorbar()
                plt.savefig('stitched_array_ensemble_' + member + '.png')
                plt.clf()
    
    print('Closing stitched output file', output_filename)
    output_file.close()
    template_input_file.close()
