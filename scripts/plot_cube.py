#!/opt/local/bin/python
from __future__ import print_function

import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from math import pi

directory = '../restarts/restartOut.Cube.1member/'
files = [directory+'grid_g' + str(side).zfill(4) + '.nc' for side in range(0,6)]
print(files)

colors = ['#0072b2', '#e69f00', '#56b4e9', '#009e73', '#f0e442', '#cc79a7']

radians_to_degrees = 180.0/pi

fig, ax = plt.subplots()
print('\n')
print('                   Untruncated Blocks                ')
print('+-----------+---------+---------+---------+---------+')
print('| Grid file | Min lat | Max lat | Min lon | Max lon |')
print('+-----------+---------+---------+---------+---------+')

for ifile, this_file in enumerate(files):
    f = netCDF4.Dataset(this_file)
    # Slice the longitude and latitude arrays to only include the lowest altitude
    lons = f.variables['Longitude'][:, :, 0]*radians_to_degrees
    lats = f.variables['Latitude'][:, :, 0]*radians_to_degrees

    print('| '+'{0: >9}'.format(str(ifile).zfill(4))+' | ' + '{0: >7}'.format(str(np.min(lats))[0:7]) + ' | ' + '{0: >7}'.format(str(np.max(lats))[0:7]) + ' | ' + '{0: >7}'.format(str(np.min(lons))[0:7]) + ' | ' + '{0: >7}'.format(str(np.max(lons))[0:7]) + ' |')
    print('+-----------+---------+---------+---------+---------+')

    ax.scatter(lons, lats, c=colors[ifile], alpha=0.3, edgecolors='none', label='Grid ' + str(ifile).zfill(4))
    f.close()

ax.legend()
plt.title('Grid file correspondence to cube sphere face')
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.savefig('../_static/cube_scatter.png', dpi=200, transparent=True, bbox_inches='tight')

# Truncate the latitudes and longitudes so there is no overlap

fig, ax = plt.subplots()
print('\n')
print('                   Truncated Blocks                  ')
print('+-----------+---------+---------+---------+---------+')
print('| Grid file | Min lat | Max lat | Min lon | Max lon |')
print('+-----------+---------+---------+---------+---------+')

for ifile, this_file in enumerate(files):
    f = netCDF4.Dataset(this_file)

    # Slice the longitude and latitude arrays to only include the lowest altitude
    lons = f.variables['Longitude'][2:-2, 2:-2, 0]*radians_to_degrees
    lats = f.variables['Latitude'][2:-2, 2:-2, 0]*radians_to_degrees

    print('| '+'{0: >9}'.format(str(ifile).zfill(4))+' | ' + '{0: >7}'.format(str(np.min(lats))[0:7]) + ' | ' + '{0: >7}'.format(str(np.max(lats))[0:7]) + ' | ' + '{0: >7}'.format(str(np.min(lons))[0:7]) + ' | ' + '{0: >7}'.format(str(np.max(lons))[0:7]) + ' |')
    print('+-----------+---------+---------+---------+---------+')

    ax.scatter(lons, lats, c=colors[ifile], alpha=0.3, edgecolors='none', label='Grid ' + str(ifile).zfill(4))
    f.close()

ax.legend(loc='lower right')
plt.title('[2:-2, 2:-2] Truncated grid file correspondence to cube sphere')
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.savefig('../_static/cube_scatter_truncated.png', dpi=200, transparent=True, bbox_inches='tight')
plt.clf()
