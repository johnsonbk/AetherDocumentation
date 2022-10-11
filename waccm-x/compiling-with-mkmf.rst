###################
Compiling with mkmf
###################

`mkmf <https://extranet.gfdl.noaa.gov/~vb/mkmf.html>`_ is a tool written in
perl and developed at GFDL that takes raw FORTRAN source code, maps out the
dependencies and then creates a ``Makefile`` to enable compilation of the code.


``mkmf`` already comes within the DART repository.  It can be used in the
following manner.

1. Run a script to stage the source code files that are intended to be compiled
2. Navigate to the DART ``build_templates`` where ``mkmf`` is located.
3. Export the location of the DART installation
4. Run mkmf
5. Use ``gmake`` to compile the code.

.. code-block::

   python ~/python_scripts/rename_i90_files.py
   cd /glade/work/johnsonb/git/DART/build_templates/
   export DART=/glade/work/johnsonb/git/DART
   ./mkmf pathnames /glade/scratch/johnsonb/mkmf_target
   make

Errors encountered
==================

seq_timemgr_mod.F90
-------------------

This file gets preprocessed by setting the `-E` flag in `config_compilers.xml`
but when it gets compiled by ``gmake``, various errors get thrown.

.. error::

   seq_timemgr_mod.F90(1988): error #6634: The shape matching rules of actual
   arguments and dummy arguments have been violated.
   call ESMF_ClockGetAlarmList(EClock, alarmListFlag, &

The unpreprocessed file has two versions of this ``ESMF_ClockGetAlarmList`` 
function that are selected by the preprocessor:

.. code-block::

   vim /glade/work/johnsonb/git/cesm2_3_0_beta09/cime/src/drivers/mct/shr/seq_timemgr_mod.F90
   [ ... ]
   1829 #ifdef USE_ESMF_LIB
   1830     allocate(EAlarm_list(AlarmCount))
   1831     call ESMF_ClockGetAlarmList(EClock, alarmListFlag=ESMF_ALARMLIST_ALL, &
   1832          alarmList=EAlarm_list, alarmCount=AlarmCount, rc=rc)
   1833 #else
   1834     call ESMF_ClockGetAlarmList(EClock, EAlarm_list, rc=rc)
   1835 #endif

ESMF_FIELD
----------

.. error::

   /glade/work/johnsonb/git/cesm2_3_0_beta09/components/cam/src/ionosphere/waccmx/utils_mod.F90(5): error #6580: Name in only-list does not exist or is not accessible.   [ESMF_FIELD]
   use esmf           ,only: ESMF_FIELD
   ----------------------------^
   compilation aborted for /glade/scratch/johnsonb/mkmf_target/utils_mod.f90 (code 1)

Comment out the use statement in the processed file:

.. code-block::

   vim /glade/scratch/johnsonb/mkmf_target/utils_mod.f90 
   ! use esmf           ,only: ESMF_FIELD

