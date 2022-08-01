.. CESM Porting Documentation documentation master file, created by
   sphinx-quickstart on Fri Oct 30 17:26:59 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

##########################
Aether Model Documentation
##########################

Welcome to the documentation of the Aether Model.

Aether is an extremely flexible community-based multi-scale
ionosphere-thermosphere model. Ensemble capability, data assimilation, and
uncertainty quantification are fundamentally integrated into the core of the
model.

Aether is an open-source model, allowing contributors from across the globe to
create, incorporate, and commit new solvers, schemes, and physics modules.

Users have straightforward defaults in the model configuration, but are able to
select any contributor's modules in order to allow for maximum flexibility.
For example, users can employ faster, less accurate solvers (for prediction)
and slower, more accurate solvers (for science).



.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Getting Started
   
   /download/github
   /download/system-requirements

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Machines

   /machines/pleiades

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Cube Sphere

   /cube-sphere/installing-cesm
   /cube-sphere/create-newcase
   /cube-sphere/grid-code
   /cube-sphere/cam
   /cube-sphere/cslam
   /cube-sphere/terminology
   /cube-sphere/pio

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: CAM Scaffolding

   /cam/advection
   /cam/atmos_phys
   /cam/chemistry
   /cam/control
   /cam/cpl
   /cam/dynamics
   /cam/ionosphere
   /cam/physics
   /cam/unit_drivers
   /cam/utils

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Data Assimilation

   data-assimilation/dart
   data-assimilation/filtering-theory

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Uncertainty Quantification

   uncertainty-quantification/monte-carlo

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Workflow

   workflow/docker

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Verification

   verification/verification-tests

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Education

   /education/coding-school

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Contributing

   /contributing/contributors-guide
   /contributing/core-team
   /contributing/rst-style-guide
   /contributing/submodules
   README

