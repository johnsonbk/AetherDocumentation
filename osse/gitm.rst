GITM Interface
##############

Overview
========

This section documents the code in DART's interface to the Global
Ionosphere–Thermosphere Model (GITM) since its latitude/longitude grid and
halo regions should be similar or identical to those implemented in the 
low-resolution configuration of Aether.

GITM Restart Files
==================

The GITM grid is partitioned into blocks which are each output in their own 
binary restart file. The naming convention for the restart files is
``bxxxx.rst``.


