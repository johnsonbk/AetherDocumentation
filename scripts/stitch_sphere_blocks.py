#!/opt/local/bin/python
from __future__ import print_function

import numpy as np
import netCDF4
import matplotlib.pyplot as plt
from math import pi

filepath = '../outputs/output.Sphere.2members/3DALL_20110320_000000_m0000.nc'

# This script takes an output file from Aether and stitches the blocks together
# to create a single 3-d array with dimensions of [lon, lat, z].

# The script assumes that there are four overlapping rows and columns at the
# interfaces of the blocks. It discards the first and last two rows and columns
# from each block.

f = netCDF4.Dataset(filepath)

ntruncate = 2
nblocks = len(f.dimensions['block'])
nlons_in_block = len(f.dimensions['lon'])
nlats_in_block = len(f.dimensions['lat'])
nzs = len(f.dimensions['z'])

# The "2*nblocks/2" syntax looks silly but it works and may be forward compatible if more blocks are introduced
nlons = nlons_in_block*nblocks/2-ntruncate*nblocks/2
nlats = nlats_in_block*nblocks/2-ntruncate*nblocks/2

stitched_array = np.empty((nlons, nlats, nzs))

o_plus = f.variables['O+']

for iblock in range(0, nblocks):
    if iblock == 0:
        stitched_array[0:nlons_in_block-ntruncate, 0:nlats_in_block-ntruncate, :] = o_plus[iblock, ntruncate:-ntruncate, ntruncate:-ntruncate]
    