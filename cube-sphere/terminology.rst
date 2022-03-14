###########
Terminology
###########


CSLAM
=====

A semi-Lagrangian, finite volume advection scheme known as the Conservative
Semi-Lagrangian Multitracer (CSLAM; Lauritzen et al., 2017 [1]_ ).

Note that when implemented in WACCM, CSLAM is four times faster than the CAM-SE
(Lauritzen, 2019 [2]_ ).

FVM
===

If CSLAM is used for advection, it uses a finite volume method (FVM) grid and
the results are then coupled to the cube-sphere grid.

GLL
===

In the SE dynamical core, the grid is known as the GLL grid because its
columns are located at the Gauss-Lobatto-Legendre quadrature points.


References
==========

.. [1] Lauritzen, P. H., M. A. Taylor, J. Overfelt, P. A. Ullrich, R. D. Nair,
       S. Goldhaber, and R. Kelly, 2017: CAM-SE–CSLAM: Consistent Coupling of a
       Conservative Semi-Lagrangian Finite-Volume Method with Spectral Element
       Dynamics. *Monthly Weather Review*, **145**, 833–855,
       https://doi.org/10.1175/MWR-D-16-0258.1.

.. [2] Lauritzen, P. H., 2019: Dynamical cores across scales in CESM.
       2019 CESM Workshop. https://www.cesm.ucar.edu/events/workshops/ws.2019/presentations/cross/lauritzen.pdf
