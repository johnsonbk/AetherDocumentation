######
CAM-SE
######

Overview
========

This page documents the attempt to understand how CAM is compiled within the 
CIME framework.

First attempt
=============

Compile a CAM-SE executable and examine the build log.

From examining the build log here, it appears that CAM is compiled as a static
library file. Library files contain a set of subprograms that are compiled into
a single binary library file.

Static libraries are bound to an executable before execution. Static libraries
have the suffix "a" which denotes "archive."

Dynamic libraries can be bound to an executable at runtime. Dynamic libraries 
have the suffix "so" which denotes "shared object."

Build log from the first attempt
--------------------------------

.. code-block::

   /glade/scratch/johnsonb/FHIST.cesm2_2_0.ne30_g17.002/bld/atm.bldlog.220611-170051.gz

Altering the gmake command for ``libatm.a`` to what it would be for a new case
(with case suffix ``.003``) results in:

.. code-block::
   
   gmake complib -j 8 MODEL=cam COMPLIB=/glade/scratch/johnsonb/FHIST.cesm2_2_0.ne30_g17.003/bld/lib/libatm.a -f
   /glade/work/johnsonb/cesm_runs/FHIST.cesm2_2_0.ne30_g17.003/Tools/Makefile
   CIME_MODEL=cesm  SMP=FALSE CASEROOT="/glade/work/johnsonb/cesm_runs/FHIST.cesm2_2_0.ne30_g17.003"
   CASETOOLS="/glade/work/johnsonb/cesm_runs/FHIST.cesm2_2_0.ne30_g17.003/Tools"
   CIMEROOT="/glade/work/johnsonb/cesm2_2_0/cime" COMP_INTERFACE="mct" COMPILER="intel"
   DEBUG="FALSE" EXEROOT="/glade/scratch/johnsonb/FHIST.cesm2_2_0.ne30_g17.003/bld"
   INCROOT="/glade/scratch/johnsonb/FHIST.cesm2_2_0.ne30_g17.003/bld/lib/include"
   LIBROOT="/glade/scratch/johnsonb/FHIST.cesm2_2_0.ne30_g17.003/bld/lib"
   MACH="cheyenne" MPILIB="mpt" NINST_VALUE="c1a1l1i1o1r1g1w1i1e1" OS="LINUX"
   PIO_VERSION="1" SHAREDLIBROOT="/glade/scratch/johnsonb/FHIST.cesm2_2_0.ne30_g17.003/bld"
   SMP_PRESENT="FALSE" USE_ESMF_LIB="FALSE" USE_MOAB="FALSE" CAM_CONFIG_OPTS="-physcam6"
   COMP_LND="clm" COMPARE_TO_NUOPC="FALSE" CISM_USE_TRILINOS="FALSE" USE_TRILINOS="FALSE"
   USE_ALBANY="FALSE" USE_PETSC="FALSE"   USER_CPPDEFS='    -DPLON=1 -DPLAT=1 -DNUM_COMP_INST_ATM=1
   -DNUM_COMP_INST_LND=1 -DNUM_COMP_INST_OCN=1 -DNUM_COMP_INST_ICE=1 -DNUM_COMP_INST_GLC=1
   -DNUM_COMP_INST_ROF=1 -DNUM_COMP_INST_WAV=1 -DNUM_COMP_INST_IAC=1 -DNUM_COMP_INST_ESP=1
   -DCAM  -D_WK_GRAD -DNP=4 -DHAVE_F2003_PTR_BND_REMAP -D_MPI -DPLEV=32 -DPCNST=33
   -DPCOLS=16 -DPSUBCOLS=1 -DN_RAD_CNST=30 -DPTRM=1 -DPTRN=1 -DPTRK=1 -DSPMD -DMODAL_AERO
   -DMODAL_AERO_4MODE  -DCLUBB_SGS -DCLUBB_CAM -DNO_LAPACK_ISNAN -DCLUBB_REAL_TYPE=dp'

When trying to run the ``gmake`` command for a case that is set up but not 
built, ``$SOURCES`` and ``$BASENAMES`` aren't set.

.. code-block::

   cd /glade/scratch/johnsonb/FHIST.cesm2_2_0.ne30_g17.002
   grep -Rl SOURCES ./
   [ ... ]
   # Returns many things
   grep -Rl BASENAMES ./
   # Returns nothing...

Second attempt
==============

This attempt will build a CESM case using ``./case.build`` after editing the
Makefile to echo the values of environmental variables.

.. code-block::

   ./create_newcase --case /glade/work/johnsonb/cesm_runs/FHIST.cesm2_2_0.ne30_g17.003 --compset FHIST --res ne30_g17 --mach cheyenne --project P86850054 --run-unsupported

What actually builds ``libatm.a``?

.. code-block::

   cd /glade/work/johnsonb/cesm_runs/FHIST.cesm2_2_0.ne30_g17.003
   grep -Rl libatm ./
   ./Tools/Makefile

I edited the Makefile to echo $(SOURCES), $(BASENAMES), $(OBJS), $(INCS):

.. code-block::

   801 #-------------------------------------------------------------------------
   802 # Build & include dependency files
   803 #-------------------------------------------------------------------------
   [ ... ]
   829 
   830 Filepath:
   831     @echo "SOURCES=$(SOURCES)"
   832     @echo "BASENAMES=$(BASENAMES)"
   833     @echo "OBJS=$(OBJS)"
   834     @echo "INCS=$(INCS)"
   835     @echo "$(VPATH)" > $@

After making the above edits, build the case:

.. code-block::

   qcmd -q share -l select=1 -A $DARES_PROJECT -- ./case.build
   [ ... ]
   Building cesm from /glade/work/johnsonb/cesm2_2_0/cime/src/drivers/mct/cime_config/buildexe with output to /glade/scratch/johnsonb/FHIST.cesm2_2_0.ne30_g17.003/bld/cesm.bldlog.220707-143352 
   Time spent not building: 52.000454 sec
   Time spent building: 1138.138125 sec
   MODEL BUILD HAS FINISHED SUCCESSFULLY

Try to find where ``$(BASENAMES)`` was echoed:

.. code-block::

   cd /glade/scratch/johnsonb/FHIST.cesm2_2_0.ne30_g17.003
   grep -Rl BASENAMES ./
   # Still returns nothing ...

Resulting object and library files
----------------------------------

All of the CAM object files are compiled here:

.. code-block::

   cd /glade/scratch/johnsonb/FHIST.cesm2_2_0.ne30_g17.003/bld/atm/obj
   ls *dyn_grid*
   dyn_grid.mod  dyn_grid.o  dyn_grid.optrpt

The actual library files are compiled here:

.. code-block::

   cd /glade/scratch/johnsonb/FHIST.cesm2_2_0.ne30_g17.003/bld/lib
   ls
   include  libatm.a  libesp.a  libglc.a  libiac.a  libice.a  libocn.a  librof.a  libwav.a

Note that ``libatm.a`` is a 53MB file.






