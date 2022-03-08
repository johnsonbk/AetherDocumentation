#########
Grid code
#########

CAM's ``dyn_grid.F90`` source code is responsible for creating a cube sphere
grid object for CAM.

According to the comments at the top of the source code, the module has two
primary responsibilites:


- Provide the physics/dynamics coupler (in module phys_grid) with data for the
  physics grid on the dynamics decomposition.

- Create CAM grid objects that are used by the I/O functionality to read
  data from an unstructured grid format to the dynamics data structures, and
  to write from the dynamics data structures to unstructured grid format.  The
  global column ordering for the unstructured grid is determined by the SE
  dycore.

