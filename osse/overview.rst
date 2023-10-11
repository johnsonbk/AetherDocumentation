OSSE Effort
###########

Overview
========

This section documents the effort to deliver an OSSE capability for Aether.
This entails assimilation of in situ state variable observations.

Miscellaneous starting points
=============================

Interpolation
-------------

Aaron's student Zehua wrote an `interpolator <https://github.com/AetherModel/Aether/blob/docs/doc/interpolation.md>`_ within the Aether source code.

Active development branch
-------------------------

The ``develop`` branch for the Aether model is far ahead of ``main`` branch.
It is accessible via the
`AetherModel/Aether repository on Github <https://github.com/AetherModel/Aether/tree/develop>`_.

Latitude/longitude grid
-----------------------

The latitude/longitude grid files are grouped in sets of four, numbered as
``0000``, ``0001``, ``0002``, ``0003``.

Headers from each of the files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- All files have a ``time`` dimension
- The ``below`` file has an ``Altitude`` dimension and an extra ``z`` index
- The ``down`` file has ``Longitude Down`` and ``Latitude Down`` and an extra ``y`` index
- The ``left`` file has ``Longitude Left`` and ``Latitude Left`` and an extra ``x`` index
- The ``corners`` file has ``Longitude Corners``, ``Latitude Corners``, ``Altitude Corners`` and an extra ``x``, ``y`` and ``z`` index
- The file without an appended descriptor has ``Longitude``, ``Latitude`` and ``Altitude``

below
~~~~~

.. code-block::

   netcdf grid_below_g0000 {
   dimensions:
           x = 22 ;
           y = 22 ;
           z = 45 ;
           time = 1 ;
   variables:
           double time(time) ;
           float Altitude Below(x, y, z) ;
                   Altitude Below:units = "meters" ;
   }

down
~~~~

.. code-block::

   netcdf grid_down_g0000 {
   dimensions:
           x = 22 ;
           y = 23 ;
           z = 44 ;
           time = 1 ;
    variables:
           double time(time) ;
           float Longitude Down(x, y, z) ;
                   Longitude Down:units = "radians" ;
           float Latitude Down(x, y, z) ;
                   Latitude Down:units = "radians" ;
   }

left
~~~~

.. code-block::

   netcdf grid_left_g0000 {
   dimensions:
           x = 23 ;
           y = 22 ;
           z = 44 ;
           time = 1 ;
   variables:
           double time(time) ;
           float Longitude Left(x, y, z) ;
                   Longitude Left:units = "radians" ;
           float Latitude Left(x, y, z) ;
                   Latitude Left:units = "radians" ;
   }

corners
~~~~~~~

.. code-block::

   netcdf grid_corners_g0000 {
   dimensions:
           x = 23 ;
           y = 23 ;
           z = 45 ;
           time = 1 ;
   variables:
           double time(time) ;
           float Longitude Corners(x, y, z) ;
                   Longitude Corners:units = "radians" ;
           float Latitude Corners(x, y, z) ;
                   Latitude Corners:units = "radians" ;
           float Altitude Corners(x, y, z) ;
                   Altitude Corners:units = "meters" ;
   }

grid
~~~~

.. code-block::

   netcdf grid_g0000 {
   dimensions:
           x = 22 ;
           y = 22 ;
           z = 44 ;
           time = 1 ;
    variables:
            double time(time) ;
            float Longitude(x, y, z) ;
                    Longitude:units = "radians" ;
            float Latitude(x, y, z) ;
                    Latitude:units = "radians" ;
            float Altitude(x, y, z) ;
                    Altitude:units = "meters" ;
   }


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

Converted to degrees, each of the four grid files has the following maximum
and minimum coordinates:

+-----------+---------+---------+---------+---------+
| Grid file | Min lat | Max lat | Min lon | Max lon |
+===========+=========+=========+=========+=========+
| g0000     | -97.5   | 7.5     | -15.0   | 195.0   |
+-----------+---------+---------+---------+---------+
| g0001     | -97.5   | 7.5     | 165.0   | 375.0   |
+-----------+---------+---------+---------+---------+
| g0002     | -7.5    | 97.5    | -15.0   | 195.0   |
+-----------+---------+---------+---------+---------+
| g0003     | -7.5    | 97.5    | 165.0   | 375.0   |
+-----------+---------+---------+---------+---------+

Truncating the grid to remove the halos
---------------------------------------

By truncating the first and last two indices from each file, the resulting plot
has no overlap of the grid files and the resulting truncated arrays have the
following maximum and minimum coordinates:

+-----------+---------+---------+---------+---------+
| Grid file | Min lat | Max lat | Min lon | Max lon |
+-----------+---------+---------+---------+---------+
|      0000 | -87.500 | -2.4999 | 5.00000 | 175.000 |
+-----------+---------+---------+---------+---------+
|      0001 | -87.500 | -2.4999 |   185.0 |   355.0 |
+-----------+---------+---------+---------+---------+
|      0002 | 2.50000 | 87.5000 | 5.00000 | 175.000 |
+-----------+---------+---------+---------+---------+
|      0003 | 2.50000 | 87.5000 |   185.0 |   355.0 |
+-----------+---------+---------+---------+---------+


|sphere_scatter_truncated|

.. |sphere_scatter_truncated| image:: /_static/sphere_scatter_truncated.png
   :width: 900
   :alt: Scatter plot of the truncated Aether latitude/longitude sphere


Cube sphere grid
----------------

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
