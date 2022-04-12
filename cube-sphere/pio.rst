############
Parallel I/O
############

The `Parallel I/O library <https://github.com/NCAR/ParallelIO>`_ enables 
applications to read and write netCDF files from a large number of processors.

CESM uses it to handle its reading and writing of netCDF files. Within the 
Common Infrastructure for Modeling the Earth (CIME) it is structured as an 
external.

.. code-block::

   cd $CESMROOT
   grep -Rl PIO_LIBDIR ./
   [ ... ]
   ./cime/scripts/Tools/Makefile
   ./cime/src/build_scripts/buildlib.pio

Makefile
========

A literal makefile used by CIME to build components.

.. code-block::

   731 CMAKE_OPTS += -D CMAKE_Fortran_FLAGS:STRING="$(FFLAGS) $(EXTRA_PIO_FPPDEFS) $(INCLDIR)" \
   732           -D CMAKE_C_FLAGS:STRING="$(CFLAGS) $(EXTRA_PIO_CPPDEFS) $(INCLDIR)" \
   733           -D CMAKE_CXX_FLAGS:STRING="$(CXXFLAGS) $(EXTRA_PIO_CPPDEFS) $(INCLDIR)" \
   734           -D CMAKE_VERBOSE_MAKEFILE:BOOL=ON \
   735           -D GPTL_PATH:STRING=$(INSTALL_SHAREDPATH) \
   736           -D PIO_ENABLE_TESTS:BOOL=OFF \
   737           -D PIO_USE_MALLOC:BOOL=ON \
   738           -D USER_CMAKE_MODULE_PATH:LIST="$(CIMEROOT)/src/CMake;$(CIMEROOT)/src/externals/pio2/cmake" \
   [ ... ]
   777 # CMake doesn't seem to like it when you define compilers via -D
   778 # CMAKE_C_COMPILER, etc., when you rerun cmake with an existing
   779 # cache. So doing this via environment variables instead.
   780 ifndef CMAKE_ENV_VARS
   781   CMAKE_ENV_VARS :=
   782 endif
   783 CMAKE_ENV_VARS += CC=$(CC) \
   784           CXX=$(CXX) \
   785           FC=$(FC) \
   786           LDFLAGS="$(LDFLAGS)"
   [ ... ]
   797 $(PIO_LIBDIR)/Makefile:
   798     cd $(PIO_LIBDIR); \
   799     $(CMAKE_ENV_VARS) cmake $(CMAKE_OPTS) $(PIO_SRC_DIR)

buildlib.pio
============

A python script that may be capable of building pio.

