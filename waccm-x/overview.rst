WACCM-X
=======

The Community Atmosphere Model (CAM) extends throughout Earth's troposphere.
The Whole Atmosphere Community Climate Model (WACCM) extends CAM further into
the stratosphere and thermosphere. The
`Whole Atmosphere Community Climate Model - eXtended (WACCM-X) <https://www2.hao.ucar.edu/sites/default/files/2021-12/WaccmxOverview.pdf>`_
is an extension of WACCM that extends upward to ~500 km altitude and includes
the ionosphere.

The overview paper of WACCM-X 2.0 (Liu et al. 2018 [1]_ ) uses the finite
volume dynamical core. The article also mentions that WACCM-X is based on CAM-4
physics and uses the ``f19`` atmospheric grid which has a horizontal resolution
of 1.9° in latitude and 2.5° in longitude.

.. important::

   It may not be possible to compile WACCM-X with the spectral element dycore.
   The safest thing to do would be to build a test case of the model with a
   finite volume dycore first.

Tutorial
========

The
`WACCM-X tutorial <https://www2.hao.ucar.edu/sites/default/files/2021-12/WACCM-Xtutorial.pdf>`_
demonstrates how to build a WACCM-X case.

.. code-block::

   cd /glade/work/johnsonb/cesm2_2_0/cime/scripts
   ./create_newcase --res f19_f19 --compset FXHIST --case /glade/work/johnsonb/cases/f.e20.FXHIST.f19_f19.001 --mach cheyenne --project $DARES_PROJECT --run-unsupported  
   cd /glade/work/johnsonb/cases/f.e20.FXHIST.f19_f19.001
   
.. note::

   Liu et al. (2018) note that the time steps for WACCM-X and CAM are
   significantly different. For example, CAM's time step for the ``f19_f19`` is
   30 minutes, while it is 5 minutes for WACCM-X. Lauritzen et al. (2017) [2]_
   note that the timestep for the roughly ~2° spectral element grid,
   ``ne16np4``, is also 30 minutes.

First attempt at building FHISTX for the ne16 grid
==================================================

.. code-block::

   cd /glade/work/johnsonb/cesm2_2_0/cime/scripts
   ./create_newcase --res ne16_g17 --compset FXHIST --case /glade/work/johnsonb/cases/f.e20.FXHIST.ne16_g17.001 --mach cheyenne --project $DARES_PROJECT --run-unsupported
   cd /glade/work/johnsonb/cases/f.e20.FXHIST.ne16_g17.001
   ./case.setup
   ./case.build

This results in the following error:

.. error::

   ERROR: Command: '/glade/work/johnsonb/cesm2_2_0/components/cam/bld/configure
   -s -fc_type intel -dyn se -hgrid ne16np4 -cpl mct -usr_src
   /glade/work/johnsonb/cases/f.e20.FXHIST.ne16_g17.001/SourceMods/src.cam
   -spmd -nosmp -ocn docn -phys cam6 -waccmx -ionosphere wxie
   -chem waccm_ma_mam4' failed with error 'ERROR:  Ionosphere is only available
   for FV dycore' from dir
   '/glade/work/johnsonb/cases/f.e20.FXHIST.ne16_g17.001/Buildconf/camconf'

This limitation in capability is also reflected in `ACOM's geospace roadmap
<https://acomstaff.acom.ucar.edu/singletrack/Documents/Geospace_Roadmap.pdf>`_.

Second attempt at building FHISTX for the ne16 grid
===================================================

This `CAM pull request <https://github.com/ESCOMP/CAM/pull/264>`_ suggests that
the limitation in the ionosphere was fixed for a more-recent version of
CAM for CESM2.3. Checkout a newer release of CESM and try again.

.. code-block::

   cd /glade/work/johnsonb
   git clone https://github.com/ESCOMP/CESM cesm2_3_0
   cd cesm2_3_0
   git checkout cesm2_3_beta01
   ./manage_externals/checkout_externals
   [ ... ]
   cd cime/scripts
   ./create_newcase --res ne16_g17 --compset FXHIST --case /glade/work/johnsonb/cases/f.e20.FXHIST.ne16_g17.002 --mach cheyenne --project $DARES_PROJECT --run-unsupported
   cd /glade/work/johnsonb/cases/f.e20.FXHIST.ne16_g17.002
   ./case.setup

.. error::

   ``ERROR:  Ionosphere is only available for FV dycore``
   
Try again to checkout a newer tag.

.. code-block::

   cd /glade/work/johnsonb
   rm -rf cesm2_3_0
   git clone https://github.com/ESCOMP/CESM cesm2_3_0
   cd cesm2_3_0
   git checkout cesm2_3_beta09
   ./manage_externals/checkout_externals
   [ ... ]
   cd cime/scripts
   ./create_newcase --res ne16_g17 --compset FXHIST --case /glade/work/johnsonb/cases/f.e20.FXHIST.ne16_g17.003 --mach cheyenne --project $DARES_PROJECT --run-unsupported

.. error::

   ``SyntaxError: invalid syntax``

Try again by checking out a slightly older tag.

.. code-block::

   git clone https://github.com/ESCOMP/CESM cesm2_3_0
   cd cesm2_3_0
   git checkout cesm2_3_beta09
   ./manage_externals/checkout_externals
   [ ... ]
   cd cime/scripts
   ./create_newcase --res ne16_g17 --compset FXHIST --case /glade/work/johnsonb/cases/f.e20.FXHIST.ne16_g17.004 --mach cheyenne --project $DARES_PROJECT --run-unsupported
   ERROR: Python 3, minor version 6 is required, you have 3.4
   source activate py37
   cd /glade/work/johnsonb/cases/f.e20.FXHIST.ne16_g17.004
   ./case.setup
   ./case.build

.. error::

   ERROR: Command /glade/work/johnsonb/cesm2_3_0/components/clm/bld/build-namelist failed rc=255
   out=
   err=ERROR : CLM build-namelist::CLMBuildNamelist::add_default() : No default value found for flanduse_timeseries.
               Are defaults provided for this resolution and land mask?

Well this is progress. 

Doing a triage of which beta releases of cesm2_3_0 provide the most plausible
path toward compilation.

References
==========

.. [1] Liu, H.-L., and Coauthors, 2018: Development and Validation of the Whole
       Atmosphere Community Climate Model With Thermosphere and Ionosphere
       Extension (WACCM-X 2.0).
       *Journal of Advances in Modeling Earth Systems*, **10**, 381–402,
       https://doi.org/10.1002/2017MS001232.

.. [2] Lauritzen, P. H., and Coauthors, 2018: NCAR Release of CAM-SE in
       CESM2.0: A Reformulation of the Spectral Element Dynamical Core in
       Dry-Mass Vertical Coordinates With Comprehensive Treatment of
       Condensates and Energy. *Journal of Advances in Modeling Earth Systems*,
       **10**, 1537–1570, https://doi.org/10.1029/2017MS001257.

