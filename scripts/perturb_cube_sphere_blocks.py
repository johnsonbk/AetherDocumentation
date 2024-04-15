#!/opt/local/bin/python
from __future__ import print_function

import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from math import pi

input_filepath = '/Users/johnsonb/work/git/AetherDocumentation/outputs/output.Cube.2members/'
input_members = ['0000', '0001']

input_prefix = '3DALL_20110320_000000_m'

output_filename_prefix = 'aether_restart_m'

output_file_prefix = input_filepath + output_filename_prefix
output_file_suffix = '.nc'

nmembers = 20
output_members = [str(member).zfill(4) for member in range(0, nmembers)]
ngrids = 6
grids = [str(grid).zfill(4) for grid in range(0, ngrids)]

scaling_factor = [member/1000.0 for member in range(-int(nmembers/2), int(nmembers/2))]

spatial_fields = ['lon', 'lat', 'z']

for ioutput_member, this_output_member in enumerate(output_members):

    for igrid, this_grid in enumerate(grids):

        input_filename = input_filepath + input_prefix + input_members[ioutput_member % 2] + '_g' + this_grid + '.nc'

        input_file = netCDF4.Dataset(input_filename)

        output_filename = output_file_prefix + this_output_member + '_g' + this_grid + '.nc'

        output_file = netCDF4.Dataset(output_filename, mode='w')

        print(output_filename)

        # Write dimensions to the output file
        nxs = len(input_file.dimensions['x'])
        nys = len(input_file.dimensions['y'])
        nzs = len(input_file.dimensions['z'])
        ntimes = len(input_file.dimensions['time'])

        x_dim = output_file.createDimension('x', nxs)
        y_dim = output_file.createDimension('y', nys)
        z_dim = output_file.createDimension('z', nzs)
        time_dim = output_file.createDimension('time', ntimes)

        time = output_file.createVariable('time', np.float64, ('time',))
        input_field = input_file.variables['time']
        time[:] = input_field[:]

        print(time)

        for ikey in input_file.variables:

            if ikey != 'time':
                input_field = input_file.variables[ikey]
                output_field = output_file.createVariable(ikey, np.float32, ('x', 'y', 'z'))
                try:
                    output_field.units = input_field.units
                except:
                    # print('No units on input field')
                    pass
                try:
                    output_field.long_name = input_field.long_name
                except:
                    # print('No long name on input field')
                    pass
                if ikey not in spatial_fields:
                    output_field[:] = input_field[:]+scaling_factor[ioutput_member]
                else:
                    output_field[:] = input_field[:]
            
        input_file.close()
        output_file.close()
