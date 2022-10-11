###############
Linking to ESMF
###############

When CIME compiles CESM, it loads the esmf_libs module to link to during
compilation.

Here is an excerpt from an  example ``software_environment.txt`` from a
successful CESM build:

.. code-block::

   vim /glade/work/johnsonb/cases/f.e230b9.FXHIST.ne30_g17.009/software_environment.txt
   Currently Loaded Modules:
   1) ncarenv/1.3    3) intel/19.1.1      5) mkl/2020.0.1              7) mpt/2.22           9) pnetcdf/1.12.2
   2) cmake/3.18.2   4) esmf_libs/8.2.0   6) esmf-8.1.1-ncdfio-mpt-O   8) netcdf-mpi/4.7.4  10) ncarcompilers/0.5.0
   [ ... ]
   ESMF_LIBDIR=/glade/p/cesmdata/cseg/PROGS/esmf/8.1.1/mpt/2.22/intel/19.1.1/lib/libO/Linux.intel.64.mpt.default

So when trying to compile this source code outside of CIME, I load the same
libraries:

.. code-block::

   module purge
   module load ncarenv/1.3 cmake intel/19.1.1 esmf_libs mkl
   module use /glade/p/cesmdata/cseg/PROGS/modulefiles/esmfpkgs/intel/19.1.1/
   module load esmf-8.1.1-ncdfio-mpt-O mpt/2.22 netcdf-mpi/4.7.4 pnetcdf/1.12.2 ncarcompilers/0.5.0

In my ``mkmf.template`` which is here:

.. code-block::

   /glade/work/johnsonb/git/DART/build_templates/mkmf.template

I reference the same library and also include an additional directory which
contains the module interface files, ``-I$(ESMF)/mod/modO/Linux.intel.64.mpt.default``:

.. code-block::

    ESMF = /glade/p/cesmdata/cseg/PROGS/esmf/8.1.1/mpt/2.22/intel/19.1.1
    INCS = -I$(NETCDF)/include -I$(ESMF)/include -I$(ESMF)/mod/modO/Linux.intel.64.mpt.default
    LIBS = -L$(NETCDF)/lib -lnetcdff -lnetcdf -L$(ESMF)/lib/libO/Linux.intel.64.mpt.default -lesmf

The file that throws a compile-time error is ``edyn_esmf.f90``. There are a few
precursor steps to running make:


.. code-block::

   python /glade/u/home/johnsonb/python_scripts/rename_i90_files.py
   cd /glade/work/johnsonb/git/DART/build_templates/
   export DART=/glade/work/johnsonb/git/DART
   ./mkmf pathnames /glade/scratch/johnsonb/mkmf_target
   make edyn_esmf.o

