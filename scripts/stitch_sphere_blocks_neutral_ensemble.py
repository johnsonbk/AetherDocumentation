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

for member in members:

    output_filename = filepath + file_prefix + member + '.nc'
    # print('Creating stitched output file', output_filename)
    output_file = netCDF4.Dataset(output_filename, mode='w')

    # Redundant preliminary step to read and write the dimensions from the 
    # grid files. This loop is the same for all members but we're repeating it
    # for the sake of making the code easier to read.

    grid_filename = filepath + 'grid_g' + blocks[0] + '.nc'
    print('Reading grid file', grid_filename)
    grid_file = netCDF4.Dataset(grid_filename)

    nlons_in_block = len(grid_file.dimensions['x'])
    nlats_in_block = len(grid_file.dimensions['y'])
    nzs = len(grid_file.dimensions['z'])

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
    time = output_file.createVariable('time', np.int32, ('time',))
    time.units = 'seconds since 1965-01-01 0 UTC'
    time.long_name = 'model time'
    input_field = grid_file.variables['time']
    time[:] = input_field[:]
    
    spatial_variables = ['Latitude', 'Longitude', 'Altitude']

    for ikey in spatial_variables:

        stitched_array = np.empty((nzs, nlons, nlats))
            
        for iblock, block in enumerate(blocks):

            grid_filename = filepath + 'grid_g' + block + '.nc'
            print('Reading grid file', grid_filename)
            grid_file = netCDF4.Dataset(grid_filename)

            input_field = grid_file.variables[ikey]
            print('ikey')

            # Loop through the z levels so that the array can be reordered from lon, lat, z to z, lat, lon
            for iz in range (0, nzs):

                for iblock in range(0, nblocks):
                    print('stitched_array[0:nlons_in_block-ntruncate, 0:nlats_in_block-ntruncate, :].shape()', stitched_array[0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate, :].shape)
                    print('input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape()', input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape)

                    if iblock == 0:
                        stitched_array[iz, 0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                    elif iblock == 1:
                        stitched_array[iz, nlons_in_block-2*ntruncate:, 0:nlats_in_block-2*ntruncate] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                    elif iblock == 2:
                        stitched_array[iz, 0:nlons_in_block-2*ntruncate, nlats_in_block-2*ntruncate:] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                    elif iblock == 3:
                        stitched_array[iz, nlons_in_block-2*ntruncate:, nlats_in_block-2*ntruncate:] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]

                stitched_array[iz, :, :] = np.transpose(stitched_array[iz, :, :])
 
        if ikey == 'Latitude':
            output_field = output_file.createVariable('lat', np.float32, ('lat'))
            output_field.units = input_field.units
            # output_field.long_name = input_field.long_name
            output_field[:] = stitched_array[0, :, 0]
        elif ikey == 'Longitude':
            output_field = output_file.createVariable('lon', np.float32, ('lon'))
            output_field.units = input_field.units
            # output_field.long_name = input_field.long_name
            output_field[:] = stitched_array[0, 0, :]
        elif ikey == 'Altitude':
            output_field = output_file.createVariable('z', np.float32, ('z'))
            output_field.units = input_field.units
            # output_field.long_name = input_field.long_name
            output_field[:] = stitched_array[:, 0, 0]

    dummy_input_filename = filepath + file_prefix + member + '_g' + blocks[0] + '.nc'
    print('Reading block file', dummy_input_filename)
    dummy_input_file = netCDF4.Dataset(dummy_input_filename)

    for ikey in dummy_input_file.variables:
        if ikey == 'time':
            pass
        else:
            formatted_key = ikey.lower().strip('\\').replace(' ', '_').replace('+','p').replace('-','n')
        
        stitched_array = np.empty((ntimes, nzs, nlons, nlats))
    
        for iblock, block in enumerate(blocks):
        
            input_filename = filepath + file_prefix + member + '_g' + block + '.nc'
            print('Reading block file', input_filename)
            input_file = netCDF4.Dataset(input_filename)
            input_field = input_file.variables[ikey]

            # Loop through the z levels so that the array can be reordered from lon, lat, z to z, lat, lon
            for iz in range (0, nzs):

                print('stitched_array[0:nlons_in_block-ntruncate, 0:nlats_in_block-ntruncate, :].shape()', stitched_array[0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate, :].shape)
                print('input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape()', input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape)

                if iblock == 0:
                    stitched_array[0, iz, 0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                elif iblock == 1:
                    stitched_array[0, iz, nlons_in_block-2*ntruncate:, 0:nlats_in_block-2*ntruncate] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                elif iblock == 2:
                    stitched_array[0, iz, 0:nlons_in_block-2*ntruncate, nlats_in_block-2*ntruncate:] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                elif iblock == 3:
                    stitched_array[0, iz, nlons_in_block-2*ntruncate:, nlats_in_block-2*ntruncate:] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]

                stitched_array[0, iz, :, :] = np.transpose(stitched_array[0, iz, :, :])
            
            input_file.close()
            
        output_field = output_file.createVariable(formatted_key, np.double, ('time', 'z', 'lat', 'lon'))
        output_field.units = input_field.units
        # output_field.long_name = input_field.long_name
        output_field[:] = stitched_array

        if formatted_key == 'temperature':

            plt.title('Temperature ('+ output_field.units  +') at highest altitude')
            plt.pcolor(np.transpose(stitched_array[0, :, :, -1]), vmin=stitched_array[0, :, :, -1].min(), vmax=stitched_array[0, :, :, -1].max())
            plt.colorbar()
            plt.savefig('stitched_array_ensemble_', member, '.png')

            plt.clf()

            plt.pcolor(input_field[2, :, :, -1], vmin=input_field[2, :, :, -1].min(), vmax=input_field[2, :, :, -1].max())
            plt.colorbar()
            plt.savefig('pcolor_on_input_field_ensemble_', member, '.png')
        

    dummy_input_file.close()
    print('Closing stitched output file', output_filename)
    output_file.close()
    

# This script takes an output file from Aether and stitches the blocks together
# to create a single 3-d array with dimensions of [lon, lat, z].

# The script assumes that there are four overlapping rows and columns at the
# interfaces of the blocks. It discards the first and last two rows and columns
# from each block.

using_old = False

if using_old:

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
    z[:] = input_field[0, 0, 0, :]

    spatial_variables = ['lat', 'lon']

    for ikey in spatial_variables:

        formatted_key = ikey.lower().strip('\\').replace(' ', '_').replace('+','p').replace('-','n')

        stitched_array = np.empty((nzs, nlons, nlats))

        input_field = input_file.variables[ikey]

        # Loop through the z levels so that the array can be reordered from lon, lat, z to z, lat, lon
        for iz in range (0, nzs):

            for iblock in range(0, nblocks):
                print('stitched_array[0:nlons_in_block-ntruncate, 0:nlats_in_block-ntruncate, :].shape()', stitched_array[0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate, :].shape)
                print('input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape()', input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape)

                if iblock == 0:
                    stitched_array[iz, 0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                elif iblock == 1:
                    stitched_array[iz, nlons_in_block-2*ntruncate:, 0:nlats_in_block-2*ntruncate] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                elif iblock == 2:
                    stitched_array[iz, 0:nlons_in_block-2*ntruncate, nlats_in_block-2*ntruncate:] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                elif iblock == 3:
                    stitched_array[iz, nlons_in_block-2*ntruncate:, nlats_in_block-2*ntruncate:] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]

            stitched_array[iz, :, :] = np.transpose(stitched_array[iz, :, :])

        if ikey == 'lat':
            output_field = output_file.createVariable(formatted_key, np.float32, ('lat'))
            output_field.units = input_field.units
            output_field.long_name = input_field.long_name
            output_field[:] = stitched_array[0, :, 0]
        elif ikey == 'lon':
            output_field = output_file.createVariable(formatted_key, np.float32, ('lon'))
            output_field.units = input_field.units
            output_field.long_name = input_field.long_name
            output_field[:] = stitched_array[0, 0, :]

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
                    print('input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape()', input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, :].shape)

                    if iblock == 0:
                        stitched_array[0, iz, 0:nlons_in_block-2*ntruncate, 0:nlats_in_block-2*ntruncate] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                    elif iblock == 1:
                        stitched_array[0, iz, nlons_in_block-2*ntruncate:, 0:nlats_in_block-2*ntruncate] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                    elif iblock == 2:
                        stitched_array[0, iz, 0:nlons_in_block-2*ntruncate, nlats_in_block-2*ntruncate:] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]
                    elif iblock == 3:
                        stitched_array[0, iz, nlons_in_block-2*ntruncate:, nlats_in_block-2*ntruncate:] = input_field[ntruncate:-ntruncate, ntruncate:-ntruncate, iz]

                stitched_array[0, iz, :, :] = np.transpose(stitched_array[0, iz, :, :])

            output_field = output_file.createVariable(formatted_key, np.double, ('time', 'z', 'lat', 'lon'))
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
