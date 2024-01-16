#!/opt/local/bin/python
from __future__ import print_function

import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from math import pi

model_work_path = '../../DART_non_merged_branch/models/aether_lon-lat/work/'
input_filepath_1 = model_work_path + 'analysis_mean.nc'
input_filepath_2 = model_work_path + 'preassim_mean.nc'
output_filepath = model_work_path + 'increments_mean.nc'

input_file_1 = netCDF4.Dataset(input_filepath_1)
input_file_2 = netCDF4.Dataset(input_filepath_2)
output_file = netCDF4.Dataset(output_filepath, 'w')

for this_dim in input_file_1.dimensions.values():
    if this_dim.isunlimited():
        output_file.createDimension(this_dim.name, None)
    else:
        output_file.createDimension(this_dim.name, this_dim.size)

for this_key in input_file_1.variables:
    input_field_1 = input_file_1.variables[this_key]
    input_field_2 = input_file_2.variables[this_key]
    
    output_field = output_file.createVariable(this_key, input_field_1.datatype, input_field_1.get_dims())
    output_field.units = input_field_1.units
    output_field.long_name = input_field_1.long_name

    # If the variable is also a dimension, do not diff between files because that will
    # result in coordinates that are all zero
    if this_key in input_file_1.dimensions:
        output_field[:] = input_field_1[:]
    else:
        output_field[:] = input_field_1[:]-input_field_2[:]

input_file_1.close()
input_file_2.close()
output_file.close()
