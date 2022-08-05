##########
atmos_phys
##########

This subdirectory is curiously not present in other versions of the repository.

- ``LICENSE.txt``
- ``README.md``
- ``kessler`` The Kessler warm rain scheme was first included to support the
  Dynamical Core.

  - ``kessler.F90`` Implements the Kessler (1969) microphysics parameterization
    as described by Soong and Ogura (1973) and Klemp and Wilhelmson (1978).
  - ``kessler.meta``
  - ``kessler_update.F90`` 
  - ``kessler_update.meta``

- ``suite_cam6.xml``
- ``suite_cam6_silhs.xml``
- ``suite_kessler.xml``
- ``utilities``

  - ``geopotential_t.F90`` Compute the geopotential height (above the surface)
    at the midpoints and interfaces using the input temperatures and pressures.
  - ``geopotential_t.meta``
  - ``state_converters.F90`` Contains various converters such as a conversion
    between temperature and potential temperature, dry pressure to dry air 
    density, wet and dry, etc.
  - ``state_converters.meta``

