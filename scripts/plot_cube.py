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

for ifile, this_file in enumerate(files):
    f = netCDF4.Dataset(this_file)
    # Slice the longitude and latitude arrays to only include the lowest altitude
    lons = f.variables['Longitude'][:, :, 0]*radians_to_degrees
    lats = f.variables['Latitude'][:, :, 0]*radians_to_degrees
    ax.scatter(lons, lats, c=colors[ifile], alpha=0.3, edgecolors='none', label='Grid ' + str(ifile).zfill(4))
    f.close()

ax.legend()
plt.title('Grid file correspondence to cube sphere face')
plt.ylabel('Latitude')
plt.xlabel('Longitude')
plt.savefig('../_static/cube_scatter.png', dpi=200, transparent=True, bbox_inches='tight')