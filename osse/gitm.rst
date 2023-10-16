GITM Interface
##############

Overview
========

This section documents the code in DART's interface to the Global
Ionosphere–Thermosphere Model (GITM) since its latitude/longitude grid and
halo regions should be similar or identical to those implemented in the 
low-resolution configuration of Aether.

.. warning::

   DART's GITM documentation isn't written in accordance with the
   recommendations in `Google's documentation style guide <https://developers.google.com/style>`_
   that DAReS staff have adopted. So there are passages such as:

   For example, this configuration of ``input.nml`` is nowhere close to being
   correct:

   .. code-block::

      &model_nml
         gitm_state_variables = 'Temperature',      'QTY_TEMPERATURE',
                                'eTemperature',     'QTY_TEMPERATURE_ELECTRON',
                                'ITemperature',     'QTY_TEMPERATURE_ION',
                                'iO_3P_NDensityS',  'QTY_DENSITY_NEUTRAL_O3P',
                                'iO2_NDensityS',    'QTY_DENSITY_NEUTRAL_O2',
                                'iN2_NDensityS',    'QTY_DENSITY_NEUTRAL_N2',
                                   ...                    ...
      /

GITM Restart Files
==================

The GITM grid is partitioned into blocks which are each output in their own 
binary restart file. The naming convention for the restart files is
``bxxxx.rst``.


