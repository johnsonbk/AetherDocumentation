#####
CSLAM
#####

Compatible grids
================

There are four grid resolutions in CAM that interface with
`CSLAM <https://ncar.github.io/CAM/doc/build/html/users_guide/atmospheric-configurations.html#cam-developmental-compsets>`_:

======================  ==================================================================
Resolution              Description
----------------------  ------------------------------------------------------------------
ne30pg3_ne30pg3_mg17    Approximately 1 degree CAM-SE-CSLAM
ne30pg2_ne30pg2_mg17    Approximately 1 degree CAM-SE-CSLAM with 1.5 degree physics grid
ne120pg3_ne120pg3_mt13  Approximately 1/4 degree CAM-SE-CSLAM
ne120pg2_ne120pg2_mt12  Approximately 1/4 degree CAM-SE-CSLAM with 3/8 degree physics grid
======================  ==================================================================

Location within CESM
====================

.. code-block::

   cd $CESMROOT
   grep -Rl CSLAM ./

* ``./components/cam/tools/topo_tool/cube_to_target/reconstruct.F90``
  
  - Provides functions for performing conservative interpolation between cubed
    sphere and lat lon grids.

* ``./components/cam/src/dynamics/se/dyn_comp.F90``
  
  - CAM interfaces to the SE Dynamical Core

* ``./components/cam/src/dynamics/se/interp_mod.F90``
  
  - Module containing subroutines and functions for interpolation.

* ``./components/cam/src/dynamics/se/dycore/global_norms_mod.F90``
  
  - Module for computing global integrals and CFL conditions

* ``./components/cam/src/dynamics/se/dycore/prim_advance_mod.F90``
  
  - Contains logic to advance the model a single timestep

* ``./components/cam/src/dynamics/se/dycore/dimensions_mod.F90``
  
  - This is a non-monophyletic module that contains node specification and
    other things such as, "scaling of viscosity in sponge layer."

* ``./components/cam/src/dynamics/se/dycore/fvm_mod.F90``
  
  - FVM_MOD File for the fvm project

* ``./components/cam/src/dynamics/se/dycore/prim_driver_mod.F90``
  
  - Primary driver mod?

* ``./components/cam/src/dynamics/se/dycore/fvm_mapping.F90``
  
  - Two things in this module:

    #. pg2->pg3 mapping as discussed in Herrington et al., 2019a [1]_ . The pg3
       grid divides each GLL grid cell into 3x3 control volumes, while the pg2
       grid divides each GLL grid cell into 2x2 control volumes. Herrington et
       al., 2019a claim that, "the effective resolution of the model is not
       degraded through the use of a coarser-resolution physics grid.
       Since the physics makes up about half the computational cost of the
       conventional CAM-SE-CSLAM configuration, the coarser physics grid may
       allow for significant cost savings with little to no downside."   
  
    #. pg3->GLL and GLL->pg3 mapping, (Herrington et al., 2019b [2]_ ) 

* ``./components/cam/src/dynamics/se/dycore/fvm_consistent_se_cslam.F90``

  - 

* ./components/cam/src/dynamics/se/dycore/prim_advection_mod.F90

* ./components/cam/src/dynamics/se/dycore/prim_state_mod.F90

* ./components/cam/src/dynamics/se/dycore/hybrid_mod.F90

* ./components/cam/src/dynamics/se/dycore/fvm_analytic_mod.F90

* ./components/cam/src/dynamics/se/dycore/fvm_control_volume_mod.F90

* ./components/cam/src/dynamics/se/restart_dynamics.F90

* ./components/cam/src/dynamics/se/dyn_grid.F90

* ./components/cam/src/dynamics/se/dp_mapping.F90

* ./ChangeLog

The meaning of the physics grid
===============================

When the documentation talks about the "physics" grid when CAM-SE is being
used, it is referring to the finite volume method grid upon which CSLAM is
being executed:

.. code-block::

   vim ./components/cam/doc/ChangeLog
   [...]
   components/cam/src/dynamics/se/dyn_comp.F90
   [...]
   the loop that sets analytic ICs for constituents directly on the
   physics grid has been removed.  Instead all constituents are initially
   set on the GLL grid, then mapped to the physics grid when CSLAM is used.
   [...]

Running the physics grid at lower resolution
============================================

Herrington et al., 2019a [1]_ show that the physics grid can be run at lower
resolution on the pg2 grid (which subdivides the cube sphere into 2x2 control
volumes) with negligible ill-effects when compared to running at a higher
resolution on the pg3 grid (which subdivides the cube sphere into 3x3 control
volumes).

References
==========

.. [1] Herrington, A. R., P. H. Lauritzen, K. A. Reed, S. Goldhaber, and B. E.
       Eaton, 2019a: Exploring a Lower-Resolution Physics Grid in CAM-SE-CSLAM.
       Journal of Advances in Modeling Earth Systems, 11, 1894–1916,
       https://doi.org/10.1029/2019MS001684.

.. [2] Herrington, A. R., P. H. Lauritzen, M. A. Taylor, S. Goldhaber, B. E.
       Eaton, J. T. Bacmeister, K. A. Reed, and P. A. Ullrich, 2019b:
       Physics–Dynamics Coupling with Element-Based High-Order Galerkin
       Methods: Quasi-Equal-Area Physics Grid. Monthly Weather Review, 147,
       69–84, https://doi.org/10.1175/MWR-D-18-0136.1.

