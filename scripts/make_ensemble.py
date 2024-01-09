#!/opt/local/bin/python
from __future__ import print_function

import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from math import pi

input_filepath = '../outputs/output.Sphere.2members/3DALL_20110320_003000_m0000_stitched.nc'

output_file_prefix = '../outputs/output.Sphere.2members/neutrals_m'
nmembers = 20
members = [str(member).zfill(4) for member in range(0, nmembers)]
output_file_suffix = '.nc'

# This script takes an output file from Aether and stitches the blocks together
# to create a single 3-d array with dimensions of [lon, lat, z].

# The script assumes that there are four overlapping rows and columns at the
# interfaces of the blocks. It discards the first and last two rows and columns
# from each block.

input_file = netCDF4.Dataset(input_filepath)
nlons = len(input_file.dimensions['lon'])
nlats = len(input_file.dimensions['lat'])
nzs = len(input_file.dimensions['z'])
ntimes = 1

scaling_factor = [member/500.0 for member in range(-int(nmembers/2), int(nmembers/2))]

for imember, this_member in enumerate(members):

    output_file = netCDF4.Dataset(output_file_prefix + this_member + output_file_suffix, mode='w')
    # Write dimensions to the output file
    time_dim = output_file.createDimension('time', None)
    z_dim = output_file.createDimension('z', nzs)
    lat_dim = output_file.createDimension('lat', nlats)
    lon_dim = output_file.createDimension('lon', nlons)

    # Write time variable to output file
    time = output_file.createVariable('time', np.int32, ('time',))
    time.units = 'seconds since 1965-01-01 0 UTC'
    time.long_name = 'model time'
    input_field = input_file.variables['time']
    time[:] = input_field[:]

    # Write z variable to output file (this is the easiest case because the entire z vector is in a single block)
    z = output_file.createVariable('z', np.float32, ('z',))
    input_field = input_file.variables['z']
    z.units = input_field.units
    z.long_name = input_field.long_name
    z[:] = input_field[:]

    lat = output_file.createVariable('lat', np.float32, ('lat'))
    input_field = input_file.variables['lat']
    lat.units = input_field.units
    lat.long_name = input_field.long_name
    lat[:] = input_field[:]
    
    lon = output_file.createVariable('lon', np.float32, ('lon'))
    input_field = input_file.variables['lon']
    lon.units = input_field.units
    lon.long_name = input_field.long_name
    lon[:] = input_field[:]

    for ikey in input_file.variables:

        if ikey == 'time' or ikey == 'lon' or ikey == 'lat' or ikey == 'z':
            pass
        else:

            stitched_array = np.empty((ntimes, nzs, nlons, nlats))

            input_field = input_file.variables[ikey]

            output_field = output_file.createVariable(ikey, np.double, ('time', 'z', 'lat', 'lon'))
            output_field.units = input_field.units
            output_field.long_name = input_field.long_name
            output_field[:] = input_field[:]+np.mean(input_field[:])*scaling_factor[imember]

        # if ikey == 'temperature':
        #     plt.title('Temperature ('+ output_field.units  +') at highest altitude')
        #     plt.pcolor(np.transpose(stitched_array[0, :, :, -1]), vmin=stitched_array[0, :, :, -1].min(), vmax=stitched_array[0, :, :, -1].max())
        #     plt.colorbar()
        #     plt.savefig('stitched_array.png')
        #     plt.clf()
        #     plt.pcolor(input_field[2, :, :, -1], vmin=input_field[2, :, :, -1].min(), vmax=input_field[2, :, :, -1].max())
        #     plt.colorbar()
        #     plt.savefig('pcolor_on_input_field.png')

    output_file.close()
