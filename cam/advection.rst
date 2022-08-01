#########
advection
#########

Contains a single subdirectory ``slt`` that has many files in it containing 
subroutines.

- ``bandij.F90`` contains a single suroutine: "Calculate longitude and latitude
  indices that identify the intervals on the extended grid that contain the
  departure points."
- ``basdy.F90`` Compute weights for the calculation of derivative estimates at
  the two center points of the four point stencil for each interval in the
  unequally spaced latitude grid. Estimates are from differentiating a 
  Lagrange cubic polynomial through the four point stencil.
- ``basdz.F90`` Compute weights for the calculation of derivative estimates at
  two center points of the four point stencil for each interval in the
  unequally spaced vertical grid (as defined by the array sig).
- ``basiy.F90`` Compute weights used in Lagrange cubic polynomial interpolation
  in the central interval of a four point stencil. Done for each interval in 
  the unequally spaced latitude grid.
- ``difcor.F90`` Add correction term to t and q horizontal diffusions and
  determine the implied heating rate due to momentum diffusion.
- ``engy_tdif.F90`` Calculate contribution of current latitude to del-T
  integral.
- ``engy_te.F90``
- ``extx.F90``
- ``extys.F90``
- ``extyv.F90``
- ``flxint.F90``
- ``grdxy.F90``
- ``hadvtest.h``
- ``hordif1.F90``
- ``kdpfnd.F90``
- ``lcbas.F90``
- ``lcdbas.F90``
- ``omcalc.F90``
- ``pdelb0.F90``
- ``phcs.F90``
- ``plevs0.F90``
- ``qmassa.F90``
- ``qmassd.F90``
- ``reordp.F90``
- ``scm0.F90``
- ``xqmass.F90``

