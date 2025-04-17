#######
Derecho
#######

Using conda to install dependencies
===================================

.. code-block::

   conda create --name aether
   conda activate aether
   conda install cmake
   conda install gcc
   conda install --channel=conda-forge armadillo
   conda install --channel=conda-forge boost
   conda install --channel=conda-forge lapack
   conda install --channel=conda-forge netcdf4
   conda install --channel=conda-forge netcdf-fortran
   conda install --channel=conda-forge netcdf-cxx4
   conda install --channel=conda-forge nlohmann_json
   conda install --channel=conda-forge mpich
   conda install --channel=conda-forge OpenBLAS

Downloading and installing aether
=================================

.. code-block::

   git clone https://github.com/AetherModel/Aether.git
   git fetch origin develop
   git switch develop
   vim CMakeLists.txt

   # edit to add path to miniconda install
   set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/share
                       # here
                       ${CMAKE_MODULE_PATH})
   :wq

   mkdir build
   cd build
   cmake -DUSE_NETCDF=ON -DUSE_FORTRAN=ON ..
   make -j32
   cd ..
   cp -R share/run ./run.test
   cd run.test
   vim run_aether.sh
   
Create a job script:

.. code-block::

   #!/usr/bin/bash
   #PBS -N run_aether
   #PBS -A REPLACE_WITH_PROJECT_CODE
   #PBS -j oe
   #PBS -k eod
   #PBS -q main
   #PBS -l walltime=00:10:00
   #PBS -l select=1:ncpus=128:mpiprocs=128
 
   $AETHERPATH/Aether/run.test/aether

Submit the job script:

.. code-block::

   qsub run_aether.sh
