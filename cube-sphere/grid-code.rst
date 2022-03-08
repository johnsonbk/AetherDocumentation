#########
Grid code
#########

CAM's ``dyn_grid.F90`` module is responsible for creating a grid object
for CAM. There are four different versions of this module:

.. code-block::

   cd /nobackup/bjohns28/CESM/components/cam/src/dynamics
   find . -name "dyn_grid.F90"
   ./se/dyn_grid.F90
   ./fv/dyn_grid.F90
   ./eul/dyn_grid.F90
   ./fv3/dyn_grid.F90

Each of these modules depends on other CAM modules, obviously, but the
intersection set of modules that all four of the ``dyn_grid.F90`` is small and
manageable.

According to the comments at the top of the source code, the module has two
primary responsibilites:

- Provide the physics/dynamics coupler (in module phys_grid) with data for the
  physics grid on the dynamics decomposition.

- Create CAM grid objects that are used by the I/O functionality to read
  data from an unstructured grid format to the dynamics data structures, and
  to write from the dynamics data structures to unstructured grid format.  The
  global column ordering for the unstructured grid is determined by the SE
  dycore.

The goal is to extract the ``se/dyn_grid.F90`` source code so that it can be
compiled without having to build the rest of the CESM code and provide a grid
object for Aether.

.. code-block::

   cd /nobackup/bjohns28/CESM/components/cam/src/
   grep -Rl dyn_grid ./
   [...]
   ./dynamics/se/dyn_comp.F90
   ./dynamics/se/interp_mod.F90
   ./dynamics/se/restart_dynamics.F90
   ./dynamics/se/gravity_waves_sources.F90
   ./dynamics/se/dp_coupling.F90
   ./dynamics/se/stepon.F90
   [...]

