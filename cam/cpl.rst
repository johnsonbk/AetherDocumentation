###
cpl
###

Has two subdirectories:

.. note::

   These source code files seem quite important. For example, the
   ``atm_comp_mct.F90`` file contains a subroutine named ``atm_init_mct``.

- ``mct``

  - ``atm_comp_mct.F90`` Contains a subroutine named ``atm_init_mct``.
  - ``atm_import_export.F90`` Contains ``atm_export``, which copies from 
    component arrays into chunk array data structure. Rearrange data from chunk
    structure into lat-lon buffer and subsequently create attribute vector.
  - ``cam_cpl_indices.F90`` Contains ``cam_cpl_indices_set`` which queries 
    booleans to determine whether certain fileds are passed by the coupler.

- ``nuopc``

  - ``atm_comp_nuopc.F90`` Contains the NUOPC cap for CAM.
  - ``atm_import_export.F90`` Contains import and export fields.
  - ``atm_shr_methods.F90`` Contains shared methods.


