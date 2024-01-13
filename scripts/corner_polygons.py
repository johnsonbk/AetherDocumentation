#!/opt/local/bin/python
from __future__ import print_function

import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from math import pi
from shapely import Polygon

directory = '../restarts/restartOut.Cube.1member/'
files = [directory+'grid_g' + str(side).zfill(4) + '.nc' for side in range(0,6)]
print(files)


# This list of colorblind safe 
colors = ['#0072b2', '#e69f00', '#56b4e9', '#009e73', '#f0e442', '#cc79a7']
# members = ['0000', '0001', '0002']
members = ['0004']
corner_files = [directory+'grid_corners_g' + member + '.nc' for member in members]

radians_to_degrees = 180.0/pi

# # Truncate the latitudes and longitudes so there is no overlap
fig, ax = plt.subplots()

for ifile, this_file in enumerate(corner_files):
    f = netCDF4.Dataset(this_file)
    # Slice the longitude and latitude arrays to only include the lowest altitude
    lons = f.variables['Longitude Corners'][2:-2, 2:-2, 0]*radians_to_degrees
    lats = f.variables['Latitude Corners'][2:-2, 2:-2, 0]*radians_to_degrees

    # This fixes the cyclic boundary condition for the most "eastward" panel
    if '0003' in this_file:
        lons[-1, :] = lons[-1, :]+360.0
    
    if '0004' in this_file:
        lons[-2:, :] = lons[-2:, :]+360.0

    print('lons.shape', lons.shape)
    print('lats.shape', lats.shape)

    nlon_centers = lons.shape[0]-1
    nlat_centers = lons.shape[1]-1

    print('nlon_centers', nlon_centers)
    print('nlat_centers', nlat_centers)

    for ilon in range(0, nlon_centers):
        for ilat in range(0, nlat_centers):
            coordinates = ((lons[ilon, ilat], lats[ilon, ilat]),
                           (lons[ilon, ilat+1], lats[ilon, ilat+1]),
                           (lons[ilon+1, ilat+1], lats[ilon+1, ilat+1]),
                           (lons[ilon+1, ilat], lats[ilon+1, ilat]),
                           (lons[ilon, ilat], lats[ilon, ilat]))
            polygon = Polygon(coordinates)
            print(polygon.area)

            xs, ys = zip(*coordinates)
            plt.plot(xs, ys)#, color=colors[ifile])

plt.show()


            

    # ax.scatter(lons, lats, c=colors[ifile], alpha=0.3333, edgecolors='none', label='Grid ' + str(ifile).zfill(4))
    # f.close()

# ax.legend()
# plt.title('Grid file correspondence to cube sphere face')
# plt.ylabel('Latitude')
# plt.xlabel('Longitude')
# plt.xlim([80, 100])
# plt.ylim([25, 45])
# plt.savefig('../_static/cube_sphere_vertex.png', dpi=200, transparent=True, bbox_inches='tight')
