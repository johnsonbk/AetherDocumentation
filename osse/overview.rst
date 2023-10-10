OSSE Effort
===========

Overview
--------

This section documents the effort to deliver an OSSE capability for Aether.
This entails assimilation of in situ state variable observations.

Miscellaneous starting points
-----------------------------

Interpolation
~~~~~~~~~~~~~

Aaron's student Zehua wrote an `interpolator <https://github.com/AetherModel/Aether/blob/docs/doc/interpolation.md>`_ within the Aether source code.

Active development branch
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``develop`` branch for the Aether model is far ahead of ``main`` branch.
It is accessible via the
`AetherModel/Aether repository on Github <https://github.com/AetherModel/Aether/tree/develop>`_.

Latitude/longitude grid
~~~~~~~~~~~~~~~~~~~~~~~

The latitude/longitude grid files are grouped in sets of four, numbered as
``0000``, ``0001``, ``0002``, ``0003``.

Using ``/scripts/plot_sphere.py`` to plot the lowest level of latitudes and
longitudes in this set of four grid files:

- ``../restarts/restartOut.Sphere.1member/grid_g0000.nc``
- ``../restarts/restartOut.Sphere.1member/grid_g0001.nc``
- ``../restarts/restartOut.Sphere.1member/grid_g0002.nc``
- ``../restarts/restartOut.Sphere.1member/grid_g0003.nc``

results in this plot that shows the overlap of the faces:

|sphere_scatter|

.. |sphere_scatter| image:: /_static/sphere_scatter.png
   :width: 900
   :alt: Scatter plot of the Aether latitude/longitude sphere

Cube sphere grid
~~~~~~~~~~~~~~~~

The cube sphere grid files are grouped in sets of six, numbered as ``0000``, 
``0001``, ``0002``, ``0003``, ``0004``, ``0005``.

Using ``/scripts/plot_cube.py`` to plot the lowest level of latitudes and
longitudes in this set of six grid files:

- ``../restarts/restartOut.Cube.1member/grid_g0000.nc``
- ``../restarts/restartOut.Cube.1member/grid_g0001.nc``
- ``../restarts/restartOut.Cube.1member/grid_g0002.nc``
- ``../restarts/restartOut.Cube.1member/grid_g0003.nc``
- ``../restarts/restartOut.Cube.1member/grid_g0004.nc``
- ``../restarts/restartOut.Cube.1member/grid_g0005.nc``

results in this plot that shows the overlap of the faces:

|cube_scatter|

.. |cube_scatter| image:: /_static/cube_scatter.png
   :width: 900
   :alt: Scatter plot of the Aether cube sphere
