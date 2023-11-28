DART model_mod
##############

This page contains notes about how the DART ``model_mod`` is implemented for
Aether.

add_domain
==========

``add_domain()`` is an interface within DART's ``state_structure_mod`` that
must be called in static_init_model().

The interface contains three subroutines:

- ``add_domain_blank`` takes model size as an argument
- ``add_domain_from_file`` takes a netcdf file and a list of variables
- ``add_domain_from_spec`` creates a skeleton of a domain and variables are
  added subsequently using ``add_dimension_to_variable``.

The last two subroutines can be called with 3 optional arguments:
``kind_list``, ``clamp_vals``, ``update_list``.

The working hypothesis is that in order for ``model_mod_check`` to match the
``quantity_of_interest = 'QTY_DENSITY_ION_OP'`` in its namelist to a variable
in the domain, that ``add_domain_from_file`` must be used and a ``kind_list``
must be passed to it.

Instead of creating a subroutine to pass the three optional variables to
``add_domain_from_file``, just define the variables in the model_mod and 
delete them later.

.. code-block::

   character(len=*), intent(in) :: info_file
   integer,          intent(in) :: num_vars
   character(len=*), intent(in) :: var_names(num_vars)
   integer,          intent(in), optional :: kind_list(num_vars)
   real(r8),         intent(in), optional :: clamp_vals(num_vars, 2)
   logical,          intent(in), optional :: update_list(num_vars)

``kind_list`` is a list of integers nvars rows long.
``clamp_vals`` is a 2 column by nvar rows list of floats containing the lower
and upper clamp values, with ``missing_r8`` to indicate no clamping.
``update_list`` is a boolean list nvars long.

obs_kind_mod
============

Contains subroutines such as ``get_index_for_quantity`` and 
``get_name_for_quantity``.

location_mod
============

.. warning::

   In the 5° configuration of Aether, thare are 36 longitude and 36 latitude 
   grid points. When entering this configuration into ``location_nml``, an
   error gets thrown when running ``model_mod_check``:

   .. code-block::

      ERROR FROM:
       source : threed_sphere/location_mod.f90
       routine: location_mod
       message: nlon is    36. Must be odd

   To get past this error, I changed ``nlon = 71`` which is the configuration 
   of GITM, but this doesn't seem correct.

model_mod_check
===============

All of the checks pass, except the rows of latitudes closest to the poles are
missing values. This may be the desired behavior, because it is unclear whether
those values can be properly interpolated.

|missing_rows|

.. |missing_rows| image:: /_static/top_bottom_rows.png

