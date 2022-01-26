######
Docker
######

In order to implement a GitHub Actions workflow in which Armadillo,
nlohmann_json, NetCDF and their dependencies can be linked or included in the
compiled model, `Docker <https://www.docker.com/>`_ can be used to create an
image on which these dependencies can be kept.

The `NetCDF documentation <https://www.unidata.ucar.edu/software/netcdf/documentation/NUG/getting_and_building_netcdf.html>`_
suggests using a package management tool to install NetCDF.

    "The easiest way to get netCDF is through a package management program,
    such as rpm, yum, homebrew, macports, adept, and others."

This document describes how to use Conda to install NetCDF and Armadillo and 
how to create a Docker image that can be activated by GitHub Actions in order
to run automated tests when pull requests are made to a specified branch.

Conda
=====

The `conda <https://conda.io/projects/conda/en/latest/index.html>`_ package
manager can quickly install the dependencies needed by Aether.

If you don't have conda installed on your system, it merely requires
downloading and running a shell script. For more information, see
`conda's installation guide <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`_.

If you would like to install the dependencies on your local machine without 
using a Docker image, the following commands create and activate a virtual
environment named ``aether-armadillo-json-netcdf`` in which the ``armadillo``
and ``nlohmann_json`` header files and the ``netcdf-cxx4`` library are
installed. 

.. code-block::

   conda create --name netcdf-armadillo-json --channel conda-forge netcdf-cxx4 armadillo nlohmann_json
   conda activate netcdf-armadillo-json

Building a Docker image
=======================

Since conda was used to install the dependencies, it's necessary to activate 
conda in a Docker file in order to create the Docker image. This `post by
Itamar Turner-Trauring <https://pythonspeed.com/articles/activate-conda-dockerfile/>`_
describes the difficulty of getting conda activate to run in the bash shell

The bash shell started by Docker isn't configured to activate a conda environment.

Building a Docker image 


 can be linked into the source code, it is useful to 

Aether's source code relies on a few dependencies in order to run properly:

- Armadillo
- NetCDF
- nlohmann JSON library

Aether manages these dependencies using `git's submodule capability
<https://git-scm.com/book/en/v2/Git-Tools-Submodules>`_. Submodules are their 
own repositories that are contained within a larger repository. Submodules can
nest within other submodules and their contents can be edited and updated.

Verify your version of git
==========================

In order to get started, you will need to verify which version of git you have
installed because git's support for submodules has changed throughout its
various releases. These instructions will work for releases equal to or newer
than git 2.7. In order to verify which version of git you are using, type:

.. code-block::

   git --version

Adding a submodule to a repository
==================================

.. code-block::

   mkdir external
   git submodule add https://github.com/nlohmann/json external/json

Modifying your git config to show the status of submodules
==========================================================

.. code-block::

   git config --global status.submoduleSummary true

Organization of the .gitmodules file
====================================

The submodules are defined in a dot file stored in the root directory of the
repository, ``.gitmodules``.

.. code-block::

   cat .gitsubmodules
   [submodule "external/json"]
       path = external/json
       url = https://github.com/nlohmann/json

Cloning a repository and its submodules
=======================================

.. code-block::

   git clone https://github.com/AetherModel/Aether.git
   cd Aether
   git submodule init 
   git submodule update

Removing a submodule from a repository
======================================

Temporary removal
-----------------

.. code-block::

   git submodule deinit external/json

Permament removal
-----------------

.. code-block::

   git submodule deinit external/json
   git rm external/json
   git commit -m "Removed json submodule"
