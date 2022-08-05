#########
advection
#########

Contains a single subdirectory ``slt``, which stands for "Semi-Lagrangian
Transport advection" that has many files in it containing subroutines.

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
- ``engy_te.F90`` Calculate contribution of current latitude to total energy.
- ``extx.F90`` Copy data to the longitude extensions of the extended array.
- ``extys.F90`` Fill latitude extensions of a scalar extended array and copy
  data to the longitude extensions of the extended array.
- ``extyv.F90`` Fill latitude extensions of a vector component extended array.
- ``flxint.F90`` Calculate contribution of current latitude to energy flux
  integral.
- ``grdxy.F90`` Define the "extended" grid used in the semi-Lagrangian
  transport scheme.
- ``hadvtest.h`` Looks like a short file that just has references to three 
  functions: ``usave``, ``vsave``, ``pssave`` in it.
- ``hordif1.F90`` Horizontal diffusion of z,d,t,q. 
- ``kdpfnd.F90`` Determine vertical departure point indices that point into a
  grid containing the full or half sigma levels.
- ``lcbas.F90`` Evaluate the partial Lagrangian cubic basis functions for the
  grid points rather than grid values.
- ``lcdbas.F90`` Calculate weights used to evaluate derivative estimates at the
  inner grid points of a four point stencil based on Lagrange cubic polynomial
  through four unequally spaced points.
- ``omcalc.F90`` Calculate vertical pressure velocity (omga = dp/dt).
- ``pdelb0.F90`` Compute the pressure intervals between the interfaces for the
  "B" portion of the hybrid grid only.
- ``phcs.F90`` Compute associated Legendre functions of the first kind of order
  m and degree n, and the associated derivatives for arg x1.
- ``plevs0.F90`` Define the pressures of the interfaces and midpoints from the
  coordinate definitions and the surface pressure.
- ``qmassa.F90`` Calculate contribution of current latitude to mass of
  constituents being advected by slt.
- ``qmassd.F90`` Compute comtribution of current latitude to global integral of
  q2*|q2 - q1|*eta.
- ``reordp.F90`` Renormalize associated Legendre polynomials and their
  derivatives.
- ``scm0.F90`` Apply SCM0 limiter to derivative estimates.
- ``xqmass.F90`` Compute comtribution of current latitude to global integrals
  necessary to compute the fixer for the non-water constituents.

