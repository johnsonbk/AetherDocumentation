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

# Write dimensions to the output file
lon_dim = output_file.createDimension('lon', nlons)
lat_dim = output_file.createDimension('lat', nlats)
z_dim = output_file.createDimension('z', nzs)
time_dim = output_file.createDimension('time', None)

# Write time variable to output file
time = output_file.createVariable('time', np.double, ('time',))
time.units = 'seconds since 1965-01-01 0 UTC'
time.long_name = 'model time'
input_field = input_file.variables['time']
time[:] = input_field[:]

for ikey in input_file.variables:
    if ikey == 'time':
        pass
    else:

        formatted_key = ikey.lower().strip('\\').replace(' ', '_').replace('+','p').replace('-','n')

        stitched_array = np.empty((nlons, nlats, nzs))

        input_field = input_file.variables[ikey]

        for iblock in range(0, nblocks):
            print('stitched_array[0:nlons_in_block-ntruncate, 0:nlats_in_block-ntruncate, :].shape()', stitched_array[0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate, :].shape)
            print('input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape()', input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape)

            if iblock == 0:
                stitched_array[0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate, :] = input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, :]
            elif iblock == 1:
                stitched_array[nlons_in_block-2*ntruncate:, 0:nlats_in_block-2*ntruncate, :] = input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, :]
            elif iblock == 2:
                stitched_array[0:nlons_in_block-2*ntruncate, nlats_in_block-2*ntruncate: :] = input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, :]
            elif iblock == 3:
                stitched_array[nlons_in_block-2*ntruncate:, nlats_in_block-2*ntruncate: :] = input_field[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate, :]

        output_field = output_file.createVariable(formatted_key, np.float32, ('lon','lat','z'))
        output_field.units = input_field.units
        output_field.long_name = input_field.long_name
        output_field[:] = stitched_array

output_file.close()

plt.pcolor(stitched_array[:, :, -1], vmin=stitched_array[:, :, -1].min(), vmax=stitched_array[:, :, -1].max())
plt.colorbar()
plt.savefig('stitched_array.png')

plt.clf()

plt.pcolor(input_field[2, :, :, -1], vmin=input_field[2, :, :, -1].min(), vmax=input_field[2, :, :, -1].max())
plt.colorbar()
plt.savefig('pcolor_on_input_field.png')

