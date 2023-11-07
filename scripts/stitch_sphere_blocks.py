#!/opt/local/bin/python
from __future__ import print_function

import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from math import pi

# filepath = '../outputs/output.Sphere.2members/3DALL_20110320_000000_m0000.nc'
input_filepath = '../outputs/output.Sphere.2members/3DALL_20110320_003000_m0000.nc'
output_filepath = '../outputs/output.Sphere.2members/3DALL_20110320_003000_m0000_stitched.nc'

# This script takes an output file from Aether and stitches the blocks together
# to create a single 3-d array with dimensions of [lon, lat, z].

# The script assumes that there are four overlapping rows and columns at the
# interfaces of the blocks. It discards the first and last two rows and columns
# from each block.

input_file = netCDF4.Dataset(input_filepath)
output_file = netCDF4.Dataset(output_filepath, mode='w')

ntruncate = 2
nblocks = len(input_file.dimensions['block'])
nlons_in_block = len(input_file.dimensions['lon'])
nlats_in_block = len(input_file.dimensions['lat'])
nzs = len(input_file.dimensions['z'])

# The "2*nblocks/2" syntax looks silly but it works and may be forward compatible if more blocks are introduced
nlons = int(nlons_in_block*nblocks/2-2*ntruncate*nblocks/2)
nlats = int(nlats_in_block*nblocks/2-2*ntruncate*nblocks/2)
print('nlons', nlons)
print('nlats', nlats)
ntimes = 1

# Write dimensions to the output file
time_dim = output_file.createDimension('time', None)
z_dim = output_file.createDimension('z', nzs)
lat_dim = output_file.createDimension('lat', nlats)
lon_dim = output_file.createDimension('lon', nlons)

# Write time variable to output file
time = output_file.createVariable('time', np.double, ('time',))
time.units = 'seconds since 1965-01-01 0 UTC'
time.long_name = 'model time'
input_field = input_file.variables['time']
time[:] = input_field[:]

# Write z variable to output file (this is the easiest case because the entire z vector is in a single block)
z = output_file.createVariable('z', np.double, ('z',))
input_field = input_file.variables['z']
z.units = input_field.units
z.long_name = input_field.long_name
z[:] = input_field[0, 0, 0, :]

spatial_variables = ['lat', 'lon']

for ikey in spatial_variables:

    formatted_key = ikey.lower().strip('\\').replace(' ', '_').replace('+','p').replace('-','n')

    stitched_array = np.empty((ntimes, nzs, nlons, nlats))

    input_field = input_file.variables[ikey]

    # Loop through the z levels so that the array can be reordered from lon, lat, z to z, lat, lon
    for iz in range (0, nzs):

        for iblock in range(0, nblocks):
            print('stitched_array[0:nlons_in_block-ntruncate, 0:nlats_in_block-ntruncate, :].shape()', stitched_array[0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate, :].shape)
            print('input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape()', input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape)

            if iblock == 0:
                stitched_array[0, iz, 0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate] = input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
            elif iblock == 1:
                stitched_array[0, iz, nlons_in_block-2*ntruncate:, 0:nlats_in_block-2*ntruncate] = input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
            elif iblock == 2:
                stitched_array[0, iz, 0:nlons_in_block-2*ntruncate, nlats_in_block-2*ntruncate:] = input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
            elif iblock == 3:
                stitched_array[0, iz, nlons_in_block-2*ntruncate:, nlats_in_block-2*ntruncate:] = input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, iz]

        stitched_array[0, iz, :, :] = np.transpose(stitched_array[0, iz, :, :])

    if ikey == 'lat':
        output_field = output_file.createVariable(formatted_key, np.float32, ('lat'))
        output_field.units = input_field.units
        output_field.long_name = input_field.long_name
        output_field[:] = stitched_array[0, 0, :, 0]
    elif ikey == 'lon':
        output_field = output_file.createVariable(formatted_key, np.float32, ('lon'))
        output_field.units = input_field.units
        output_field.long_name = input_field.long_name
        output_field[:] = stitched_array[0, 0, 0, :]


for ikey in input_file.variables:
    if ikey == 'time' or ikey == 'lon' or ikey == 'lat' or ikey == 'z':
        pass
    else:

        formatted_key = ikey.lower().strip('\\').replace(' ', '_').replace('+','p').replace('-','n')

        stitched_array = np.empty((ntimes, nzs, nlons, nlats))

        input_field = input_file.variables[ikey]

        # Loop through the z levels so that the array can be reordered from lon, lat, z to z, lat, lon
        for iz in range (0, nzs):

            for iblock in range(0, nblocks):
                print('stitched_array[0:nlons_in_block-ntruncate, 0:nlats_in_block-ntruncate, :].shape()', stitched_array[0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate, :].shape)
                print('input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape()', input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape)

                if iblock == 0:
                    stitched_array[0, iz, 0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate] = input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                elif iblock == 1:
                    stitched_array[0, iz, nlons_in_block-2*ntruncate:, 0:nlats_in_block-2*ntruncate] = input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                elif iblock == 2:
                    stitched_array[0, iz, 0:nlons_in_block-2*ntruncate, nlats_in_block-2*ntruncate:] = input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                elif iblock == 3:
                    stitched_array[0, iz, nlons_in_block-2*ntruncate:, nlats_in_block-2*ntruncate:] = input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, iz]

            stitched_array[0, iz, :, :] = np.transpose(stitched_array[0, iz, :, :])

        output_field = output_file.createVariable(formatted_key, np.float32, ('time', 'z', 'lat', 'lon'))
        output_field.units = input_field.units
        output_field.long_name = input_field.long_name
        output_field[:] = stitched_array

        if formatted_key == 'temperature':

            plt.title('Temperature ('+ output_field.units  +') at highest altitude')
            plt.pcolor(np.transpose(stitched_array[0, :, :, -1]), vmin=stitched_array[0, :, :, -1].min(), vmax=stitched_array[0, :, :, -1].max())
            plt.colorbar()
            plt.savefig('stitched_array.png')

            plt.clf()

            plt.pcolor(input_field[2, :, :, -1], vmin=input_field[2, :, :, -1].min(), vmax=input_field[2, :, :, -1].max())
            plt.colorbar()
            plt.savefig('pcolor_on_input_field.png')

output_file.close()
