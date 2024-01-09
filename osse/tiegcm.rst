TIEGCM Interface
################

Overview
========

This section documents the code in DARTs interface to the Thermosphere
Ionosphere Electrodynamics General Circulation Model (TIEGCM).

DARTs TIEGCM interface implements current best practices within the code base.

The default TIEGCM state variables listed in ``input.nml`` and their
corresponding DART quantities are as follows:

+----------------+----------------------------------------+
| TIEGCM key     | DART quantity                          |
+================+========================================+
| ``NE``         | ``QTY_ELECTRON_DENSITY``               |
+----------------+----------------------------------------+
| ``OP``         | ``QTY_DENSITY_ION_OP``                 |
+----------------+----------------------------------------+
| ``TI``         | ``QTY_TEMPERATURE_ION``                |
+----------------+----------------------------------------+
| ``TE``         | ``QTY_TEMPERATURE_ELECTRON``           |
+----------------+----------------------------------------+
| ``OP_NM``      | ``QTY_DENSITY_ION_OP``                 |
+----------------+----------------------------------------+
| ``O1``         | ``QTY_ATOMIC_OXYGEN_MIXING_RATIO``     |
+----------------+----------------------------------------+
| ``O2``         | ``QTY_MOLEC_OXYGEN_MIXING_RATIO``      |
+----------------+----------------------------------------+
| ``TN``         | ``QTY_TEMPERATURE``                    |
+----------------+----------------------------------------+
| ``ZG``         | ``QTY_GEOMETRIC_HEIGHT``               |
+----------------+----------------------------------------+

.. note::

   Next step: run TIEGCM quickbuild to see if model_mod_check produces the
   same results as Aether.

``model_mod_check`` throws an error because ``ZG`` is not in the file.

.. error::

   ERROR FROM:
      source : netcdf_utilities_mod.f90
      routine: load_variable_ids, nf90_inq_var_id
      message:  domain            2 , variable #           1  "ZG" from file "tiegcm_s.nc": NetCDF: Variable not found
      message: ...

Got the proper restart files from Helen and ``model_mod_check`` runs properly.

Getting a test case running
===========================

Downloaded files from Helen's restart directory:

.. code-block::

   sftp <user>@data-access.ucar.edu
   cd /glade/work/hkershaw/DART/TIEGCM/initial/
   get tiegcm_restart_p.nc.000[12345]
   get tiegcm_s.nc.000[12345]

Helen also has a directory with suitable obs_seq files:

.. code-block::

   get /glade/work/hkershaw/tiegcm/dart-tiegcm/dart/observations/iono/work/obs_seq.out.01

The time is inconsistet between the obs_seq file and the restart files.

Editing the obs_seq file
~~~~~~~~~~~~~~~~~~~~~~~~

Truncate the obs_seq file to only have two observations:

1. Set ``num_obs`` and ``max_num_obs`` to ``2``.
2. Change the middle integer of the linked list row for the second observation to ``-1``.

There are two types of errors that DART throws if there's a time inconsistency between
the restart and obs_seq files.

This error was thrown when the observations were before the model timestep:

.. error::

   .. code-block::

      message: Inconsistent model state/observation times, cannot continue
      message: ... If this is the start of the obs_seq file,
      message: ... can use filter namelist to set first obs or initial data time.

In order to fix it, change the following entries in ``filter_nml`` to match the restart
time of the model.

.. code-block::

   init_time_days               = 148827,
   init_time_seconds            = 0,

This error was thrown when the day was correct but the observations were outside the observation
window. It was fixed by changing the seconds of the observation to be within the window.

.. error::

   .. code-block::

      message: advancing the model inside filter and multiple file output not currently supported``

.. code-block::

   obs_sequence
   obs_kind_definitions
            1
            38 GPS_PROFILE                     
   num_copies:            1  num_qc:            1
   num_obs:               2  max_num_obs:       2
   observations                                                    
   Ionprf QC                                                       
   first:            1  last:        2
   OBS            1
      29938.9975872335     
   0.000000000000000E+000
            -1           2          -1
   obdef
   loc3d
      0.6364235585050975         1.203183856656520         150000.0000000000      3
   kind
            38
   900     148827
      248062484.510243     
   OBS            2
      27450.2966235645     
   0.000000000000000E+000
            1           -1          -1
   obdef
   loc3d
      0.6328654506936452         1.201456558337492         200000.0000000000      3
   kind
            38
   900     148827
      440999972.462655
