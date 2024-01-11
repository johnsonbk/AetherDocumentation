#!/opt/local/bin/python
from __future__ import print_function

import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from math import pi

directory = '../restarts/restartOut.Cube.1member/'
files = [directory+'grid_g' + str(side).zfill(4) + '.nc' for side in range(0,6)]
print(files)


# This list of colorblind safe 
# colors = ['#0072b2', '#e69f00', '#56b4e9', '#009e73', '#f0e442', '#cc79a7']

colors = ['#FF0000', '#00FF00', '#0000FF']
members = ['0000', '0001', '0005']
center_files = [directory+'grid_g' + member + '.nc' for member in members]
corner_files = [directory+'grid_corners_g' + member + '.nc' for member in members]

radians_to_degrees = 180.0/pi

fig, ax = plt.subplots()

for ifile, this_file in enumerate(center_files):
    f = netCDF4.Dataset(this_file)
    # Slice the longitude and latitude arrays to only include the lowest altitude
    lons = f.variables['Longitude'][:, :, 0]*radians_to_degrees
    lats = f.variables['Latitude'][:, :, 0]*radians_to_degrees
    ax.scatter(lons, lats, c=colors[ifile], alpha=0.7, edgecolors='none', label='Grid ' + str(ifile).zfill(4))
    f.close()

for ifile, this_file in enumerate(corner_files):
    f = netCDF4.Dataset(this_file)
    # Slice the longitude and latitude arrays to only include the lowest altitude
    lons = f.variables['Longitude Corners'][:, :, 0]*radians_to_degrees
    lats = f.variables['Latitude Corners'][:, :, 0]*radians_to_degrees
    ax.scatter(lons, lats, c=colors[ifile], alpha=0.2, edgecolors='none', label='Grid ' + str(ifile).zfill(4))
    f.close()

ax.legend()
plt.title('Grid file correspondence to cube sphere face')
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.savefig('../_static/cube_scatter_corners_vertices.png', dpi=200, transparent=True, bbox_inches='tight')
plt.clf()

# # Truncate the latitudes and longitudes so there is no overlap
fig, ax = plt.subplots()

for ifile, this_file in enumerate(center_files):
    f = netCDF4.Dataset(this_file)
    # Slice the longitude and latitude arrays to only include the lowest altitude
    lons = f.variables['Longitude'][2:-2, 2:-2, 0]*radians_to_degrees
    lats = f.variables['Latitude'][2:-2, 2:-2, 0]*radians_to_degrees
    ax.scatter(lons, lats, c=colors[ifile], alpha=1.0, edgecolors='none', label='Grid ' + str(ifile).zfill(4))
    f.close()

for ifile, this_file in enumerate(corner_files):
    f = netCDF4.Dataset(this_file)
    # Slice the longitude and latitude arrays to only include the lowest altitude
    lons = f.variables['Longitude Corners'][2:-2, 2:-2, 0]*radians_to_degrees
    lats = f.variables['Latitude Corners'][2:-2, 2:-2, 0]*radians_to_degrees
    ax.scatter(lons, lats, c=colors[ifile], alpha=0.3333, edgecolors='none', label='Grid ' + str(ifile).zfill(4))
    f.close()

# ax.legend()
plt.title('Grid file correspondence to cube sphere face')
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.xlim([80, 100])
plt.ylim([25, 45])
plt.savefig('../_static/cube_sphere_vertex.png', dpi=200, transparent=True, bbox_inches='tight')
