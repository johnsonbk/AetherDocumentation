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
   ./cime/.git/objects/pack/pack-d288870650375a49cb6725099b980651a9e84f25.pack
   ./components/cam/tools/topo_tool/cube_to_target/reconstruct.F90
   ./components/cam/doc/ChangeLog
   ./components/cam/cime_config/testdefs/testlist_cam.xml
   ./components/cam/bld/namelist_files/namelist_definition.xml
   ./components/cam/src/dynamics/se/dyn_comp.F90
   ./components/cam/src/dynamics/se/interp_mod.F90
   ./components/cam/src/dynamics/se/dycore/global_norms_mod.F90
   ./components/cam/src/dynamics/se/dycore/prim_advance_mod.F90
   ./components/cam/src/dynamics/se/dycore/dimensions_mod.F90
   ./components/cam/src/dynamics/se/dycore/fvm_mod.F90
   ./components/cam/src/dynamics/se/dycore/prim_driver_mod.F90
   ./components/cam/src/dynamics/se/dycore/fvm_mapping.F90
   ./components/cam/src/dynamics/se/dycore/fvm_consistent_se_cslam.F90
   ./components/cam/src/dynamics/se/dycore/prim_advection_mod.F90
   ./components/cam/src/dynamics/se/dycore/prim_state_mod.F90
   ./components/cam/src/dynamics/se/dycore/hybrid_mod.F90
   ./components/cam/src/dynamics/se/dycore/fvm_analytic_mod.F90
   ./components/cam/src/dynamics/se/dycore/fvm_control_volume_mod.F90
   ./components/cam/src/dynamics/se/restart_dynamics.F90
   ./components/cam/src/dynamics/se/dyn_grid.F90
   ./components/cam/src/dynamics/se/dp_mapping.F90
   ./ChangeLog

The meaning of the "physics" grid
=================================

Judging from context, when the documentation talks about the "physics" grid 
when CAM-SE is being used, it is referring to the finite volume method grid
upon which CSLAM is being executed:

.. code-block::

   vim ./components/cam/doc/ChangeLog
   [...]
   components/cam/src/dynamics/se/dyn_comp.F90
   [...]
   the loop that sets analytic ICs for constituents directly on the
   physics grid has been removed.  Instead all constituents are initially
   set on the GLL grid, then mapped to the physics grid when CSLAM is used.
   [...]

