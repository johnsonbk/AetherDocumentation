####
DART
####

The Data Assimilation Research Testbed (DART) implements many ensemble
assimilation methodologies including the Ensemble Kalman Filter (Evensen, 2003)
[1]_ and the Ensemble Adjustment Kalman Filter (Anderson, 2001). [2]_

Forward operators required to assimilate observations perform line-of-sight
integration, volume integration, interpolation, and other common techniques.

These forward operators are optimized given the grid structures and the
parallelization scheme.

References
==========

.. [1] Evensen, G., 2003: The Ensemble Kalman Filter: theoretical formulation
       and practical implementation. *Ocean Dynamics*, **53**, 343–367,
       `doi:10.1007/s10236-003-0036-9 <https://doi.org/10.1007/s10236-003-0036-9>`_

.. [2] Anderson, J. L., 2001: An Ensemble Adjustment Kalman Filter for Data
       Assimilation. *Monthly Weather Review*, **129**, 2884-2903,
       `doi:10.1175/1520-0493(2001)129\<2884:AEAKFF\>2.0.CO;2 <http://dx.doi.org/10.1175/1520-0493(2001)129%3C2884%3AAEAKFF%3E2.0.CO%3B2>`_