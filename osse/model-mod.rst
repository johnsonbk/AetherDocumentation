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

