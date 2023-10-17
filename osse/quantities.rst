Quantities
##########

Aether's state variable keys must be mapped to DART quantities.

.. note::

   We might run into problems with escaped spaces because Aether variable keys
   are inconsistent with `CF Metadata Conventions <https://cfconventions.org/>`_
   which state, "Variable, dimension, attribute and group names should begin
   with a letter and be composed of letters, digits, and underscores."
   For example the Aether variable key corresponding to ``QTY_TEMPERATURE_ION``
   is ``Bulk\ Ion\ Temperature``.

The Aether variables in the table below match eight of the nine variables in
DART's default configuration of ``model_nml`` for TIEGCM. The omitted TIEGCM
variable is ``OP_NM`` which has the long name ``OP (TIME N-1)``.

+--------------------------------+-----------------------------------+----------------------------------------+
| Aether key                     | File contained within             | DART quantity                          |
+================================+===================================+========================================+
| ``e-``                         | ``3DALL_20110320_000000_m0000``   | ``QTY_ELECTRON_DENSITY``               |
+--------------------------------+-----------------------------------+----------------------------------------+
| ``O+``                         | ``3DALL_20110320_000000_m0000``   | ``QTY_DENSITY_ION_OP``                 |
+--------------------------------+-----------------------------------+----------------------------------------+
| ``Bulk\ Ion\ Temperature``     | ``3DALL_20110320_000000_m0000``   | ``QTY_TEMPERATURE_ION``                |
+--------------------------------+-----------------------------------+----------------------------------------+
| ``e-\ Temperature``            | ``3DALL_20110320_000000_m0000``   | ``QTY_TEMPERATURE_ELECTRON``           |
+--------------------------------+-----------------------------------+----------------------------------------+
| ``O1``                         | ``3DALL_20110320_000000_m0000``   | ``QTY_ATOMIC_OXYGEN_MIXING_RATIO``     |
+--------------------------------+-----------------------------------+----------------------------------------+
| ``O2``                         | ``3DALL_20110320_000000_m0000``   | ``QTY_MOLEC_OXYGEN_MIXING_RATIO``      |
+--------------------------------+-----------------------------------+----------------------------------------+
| ``Temperature``                | ``3DALL_20110320_000000_m0000``   | ``QTY_TEMPERATURE``                    |
+--------------------------------+-----------------------------------+----------------------------------------+
| ``z``                          | ``3DALL_20110320_000000_m0000``   | ``QTY_GEOMETRIC_HEIGHT``               |
+--------------------------------+-----------------------------------+----------------------------------------+

ions_m0000_g0000 
~~~~~~~~~~~~~~~~

.. code-block::

   netcdf ions_m0000_g0000 {
   dimensions:
       x = 22 ;
       y = 22 ;
       z = 44 ;
       time = 1 ;
   variables:
       double time(time) ;
       float O+(x, y, z) ;
           O+:units = "/m3" ;
       float Temperature\ \(O+\)(x, y, z) ;
           Temperature\ \(O+\):units = "K" ;
       float Parallel\ Ion\ Velocity\ \(Zonal\)\ \(O+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Zonal\)\ \(O+\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Meridional\)\ \(O+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Meridional\)\ \(O+\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Vertical\)\ \(O+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Vertical\)\ \(O+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Zonal\)\ \(O+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Zonal\)\ \(O+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Meridional\)\ \(O+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Meridional\)\ \(O+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Vertical\)\ \(O+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Vertical\)\ \(O+\):units = "m/s" ;
       float O2+(x, y, z) ;
           O2+:units = "/m3" ;
       float Temperature\ \(O2+\)(x, y, z) ;
           Temperature\ \(O2+\):units = "K" ;
       float Parallel\ Ion\ Velocity\ \(Zonal\)\ \(O2+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Zonal\)\ \(O2+\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Meridional\)\ \(O2+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Meridional\)\ \(O2+\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Vertical\)\ \(O2+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Vertical\)\ \(O2+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Zonal\)\ \(O2+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Zonal\)\ \(O2+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Meridional\)\ \(O2+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Meridional\)\ \(O2+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Vertical\)\ \(O2+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Vertical\)\ \(O2+\):units = "m/s" ;
       float N2+(x, y, z) ;
           N2+:units = "/m3" ;
       float Temperature\ \(N2+\)(x, y, z) ;
           Temperature\ \(N2+\):units = "K" ;
       float Parallel\ Ion\ Velocity\ \(Zonal\)\ \(N2+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Zonal\)\ \(N2+\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Meridional\)\ \(N2+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Meridional\)\ \(N2+\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Vertical\)\ \(N2+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Vertical\)\ \(N2+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Zonal\)\ \(N2+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Zonal\)\ \(N2+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Meridional\)\ \(N2+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Meridional\)\ \(N2+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Vertical\)\ \(N2+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Vertical\)\ \(N2+\):units = "m/s" ;
       float NO+(x, y, z) ;
           NO+:units = "/m3" ;
       float Temperature\ \(NO+\)(x, y, z) ;
           Temperature\ \(NO+\):units = "K" ;
       float Parallel\ Ion\ Velocity\ \(Zonal\)\ \(NO+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Zonal\)\ \(NO+\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Meridional\)\ \(NO+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Meridional\)\ \(NO+\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Vertical\)\ \(NO+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Vertical\)\ \(NO+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Zonal\)\ \(NO+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Zonal\)\ \(NO+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Meridional\)\ \(NO+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Meridional\)\ \(NO+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Vertical\)\ \(NO+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Vertical\)\ \(NO+\):units = "m/s" ;
       float N+(x, y, z) ;
           N+:units = "/m3" ;
       float Temperature\ \(N+\)(x, y, z) ;
           Temperature\ \(N+\):units = "K" ;
       float Parallel\ Ion\ Velocity\ \(Zonal\)\ \(N+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Zonal\)\ \(N+\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Meridional\)\ \(N+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Meridional\)\ \(N+\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Vertical\)\ \(N+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Vertical\)\ \(N+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Zonal\)\ \(N+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Zonal\)\ \(N+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Meridional\)\ \(N+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Meridional\)\ \(N+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Vertical\)\ \(N+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Vertical\)\ \(N+\):units = "m/s" ;
       float He+(x, y, z) ;
           He+:units = "/m3" ;
       float Temperature\ \(He+\)(x, y, z) ;
           Temperature\ \(He+\):units = "K" ;
       float Parallel\ Ion\ Velocity\ \(Zonal\)\ \(He+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Zonal\)\ \(He+\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Meridional\)\ \(He+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Meridional\)\ \(He+\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Vertical\)\ \(He+\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Vertical\)\ \(He+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Zonal\)\ \(He+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Zonal\)\ \(He+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Meridional\)\ \(He+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Meridional\)\ \(He+\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Vertical\)\ \(He+\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Vertical\)\ \(He+\):units = "m/s" ;
       float O+2D(x, y, z) ;
           O+2D:units = "/m3" ;
       float Temperature\ \(O+2D\)(x, y, z) ;
           Temperature\ \(O+2D\):units = "K" ;
       float Parallel\ Ion\ Velocity\ \(Zonal\)\ \(O+2D\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Zonal\)\ \(O+2D\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Meridional\)\ \(O+2D\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Meridional\)\ \(O+2D\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Vertical\)\ \(O+2D\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Vertical\)\ \(O+2D\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Zonal\)\ \(O+2D\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Zonal\)\ \(O+2D\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Meridional\)\ \(O+2D\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Meridional\)\ \(O+2D\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Vertical\)\ \(O+2D\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Vertical\)\ \(O+2D\):units = "m/s" ;
       float O+2P(x, y, z) ;
           O+2P:units = "/m3" ;
       float Temperature\ \(O+2P\)(x, y, z) ;
           Temperature\ \(O+2P\):units = "K" ;
       float Parallel\ Ion\ Velocity\ \(Zonal\)\ \(O+2P\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Zonal\)\ \(O+2P\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Meridional\)\ \(O+2P\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Meridional\)\ \(O+2P\):units = "m/s" ;
       float Parallel\ Ion\ Velocity\ \(Vertical\)\ \(O+2P\)(x, y, z) ;
           Parallel\ Ion\ Velocity\ \(Vertical\)\ \(O+2P\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Zonal\)\ \(O+2P\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Zonal\)\ \(O+2P\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Meridional\)\ \(O+2P\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Meridional\)\ \(O+2P\):units = "m/s" ;
       float Perp.\ Ion\ Velocity\ \(Vertical\)\ \(O+2P\)(x, y, z) ;
           Perp.\ Ion\ Velocity\ \(Vertical\)\ \(O+2P\):units = "m/s" ;
       float Temperature\ \(bulk\ ion\)(x, y, z) ;
           Temperature\ \(bulk\ ion\):units = "K" ;
       float Temperature\ \(electron\)(x, y, z) ;
           Temperature\ \(electron\):units = "K" ;
   }

neutrals_m0000_g0000
~~~~~~~~~~~~~~~~~~~~

.. code-block::

   netcdf neutrals_m0000_g0000 {
   dimensions:
       x = 22 ;
       y = 22 ;
       z = 44 ;
       time = 1 ;
   variables:
       double time(time) ;
       float O(x, y, z) ;
           O:units = "/m3" ;
       float N_4S(x, y, z) ;
           N_4S:units = "/m3" ;
       float O2(x, y, z) ;
           O2:units = "/m3" ;
       float N2(x, y, z) ;
           N2:units = "/m3" ;
       float NO(x, y, z) ;
           NO:units = "/m3" ;
       float He(x, y, z) ;
           He:units = "/m3" ;
       float N_2D(x, y, z) ;
           N_2D:units = "/m3" ;
       float N_2P(x, y, z) ;
           N_2P:units = "/m3" ;
       float H(x, y, z) ;
           H:units = "/m3" ;
       float O_1D(x, y, z) ;
           O_1D:units = "/m3" ;
       float CO2(x, y, z) ;
           CO2:units = "/m3" ;
       float Temperature(x, y, z) ;
           Temperature:units = "K" ;
       float Zonal\ Wind(x, y, z) ;
           Zonal\ Wind:units = "m/s" ;
       float Meridional\ Wind(x, y, z) ;
           Meridional\ Wind:units = "m/s" ;
       float Vertical\ Wind(x, y, z) ;
           Vertical\ Wind:units = "m/s" ;
   }

3DALL_20110320_000000_m0000
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

   netcdf \3DALL_20110320_000000_m0000 {
   dimensions:
       lon = 22 ;
       lat = 22 ;
       z = 44 ;
       block = UNLIMITED ; // (4 currently)
       time = UNLIMITED ; // (1 currently)
   variables:
       double time(time) ;
       float lon(block, lon, lat, z) ;
           lon:units = "degrees_east" ;
           lon:long_name = "longitude" ;
       float lat(block, lon, lat, z) ;
           lat:units = "degrees_north" ;
           lat:long_name = "latitude" ;
       float z(block, lon, lat, z) ;
           z:units = "m" ;
           z:long_name = "height above mean sea level" ;
       float O(block, lon, lat, z) ;
           O:units = "/m3" ;
           O:long_name = "O" ;
       float N_4S(block, lon, lat, z) ;
           N_4S:units = "/m3" ;
           N_4S:long_name = "N_4S" ;
       float O2(block, lon, lat, z) ;
           O2:units = "/m3" ;
           O2:long_name = "O2" ;
       float N2(block, lon, lat, z) ;
           N2:units = "/m3" ;
           N2:long_name = "N2" ;
       float NO(block, lon, lat, z) ;
           NO:units = "/m3" ;
           NO:long_name = "NO" ;
       float He(block, lon, lat, z) ;
           He:units = "/m3" ;
           He:long_name = "He" ;
       float N_2D(block, lon, lat, z) ;
           N_2D:units = "/m3" ;
           N_2D:long_name = "N_2D" ;
       float N_2P(block, lon, lat, z) ;
           N_2P:units = "/m3" ;
           N_2P:long_name = "N_2P" ;
       float H(block, lon, lat, z) ;
           H:units = "/m3" ;
           H:long_name = "H" ;
       float O_1D(block, lon, lat, z) ;
           O_1D:units = "/m3" ;
           O_1D:long_name = "O_1D" ;
       float CO2(block, lon, lat, z) ;
           CO2:units = "/m3" ;
           CO2:long_name = "CO2" ;
       float Temperature(block, lon, lat, z) ;
           Temperature:units = "K" ;
           Temperature:long_name = "Temperature" ;
       float Zonal\ Wind(block, lon, lat, z) ;
           Zonal\ Wind:units = "m/s" ;
           Zonal\ Wind:long_name = "Zonal Wind" ;
       float Meridional\ Wind(block, lon, lat, z) ;
           Meridional\ Wind:units = "m/s" ;
           Meridional\ Wind:long_name = "Meridional Wind" ;
       float Vertical\ Wind(block, lon, lat, z) ;
           Vertical\ Wind:units = "m/s" ;
           Vertical\ Wind:long_name = "Vertical Wind" ;
       float O+(block, lon, lat, z) ;
           O+:units = "/m3" ;
           O+:long_name = "O+" ;
       float O2+(block, lon, lat, z) ;
           O2+:units = "/m3" ;
           O2+:long_name = "O2+" ;
       float N2+(block, lon, lat, z) ;
           N2+:units = "/m3" ;
           N2+:long_name = "N2+" ;
       float NO+(block, lon, lat, z) ;
           NO+:units = "/m3" ;
           NO+:long_name = "NO+" ;
       float N+(block, lon, lat, z) ;
           N+:units = "/m3" ;
           N+:long_name = "N+" ;
       float He+(block, lon, lat, z) ;
           He+:units = "/m3" ;
           He+:long_name = "He+" ;
       float O+2D(block, lon, lat, z) ;
           O+2D:units = "/m3" ;
           O+2D:long_name = "O+2D" ;
       float O+2P(block, lon, lat, z) ;
           O+2P:units = "/m3" ;
           O+2P:long_name = "O+2P" ;
       float e-(block, lon, lat, z) ;
           e-:units = "/m3" ;
           e-:long_name = "e-" ;
       float O+\ Temperature(block, lon, lat, z) ;
           O+\ Temperature:units = "K" ;
           O+\ Temperature:long_name = "O+ Temperature" ;
       float O2+\ Temperature(block, lon, lat, z) ;
           O2+\ Temperature:units = "K" ;
           O2+\ Temperature:long_name = "O2+ Temperature" ;
       float N2+\ Temperature(block, lon, lat, z) ;
           N2+\ Temperature:units = "K" ;
           N2+\ Temperature:long_name = "N2+ Temperature" ;
       float NO+\ Temperature(block, lon, lat, z) ;
           NO+\ Temperature:units = "K" ;
           NO+\ Temperature:long_name = "NO+ Temperature" ;
       float N+\ Temperature(block, lon, lat, z) ;
           N+\ Temperature:units = "K" ;
           N+\ Temperature:long_name = "N+ Temperature" ;
       float He+\ Temperature(block, lon, lat, z) ;
           He+\ Temperature:units = "K" ;
           He+\ Temperature:long_name = "He+ Temperature" ;
       float O+2D\ Temperature(block, lon, lat, z) ;
           O+2D\ Temperature:units = "K" ;
           O+2D\ Temperature:long_name = "O+2D Temperature" ;
       float O+2P\ Temperature(block, lon, lat, z) ;
           O+2P\ Temperature:units = "K" ;
           O+2P\ Temperature:long_name = "O+2P Temperature" ;
       float e-\ Temperature(block, lon, lat, z) ;
           e-\ Temperature:units = "K" ;
           e-\ Temperature:long_name = "e- Temperature" ;
       float Bulk\ Ion\ Temperature(block, lon, lat, z) ;
           Bulk\ Ion\ Temperature:units = "K" ;
           Bulk\ Ion\ Temperature:long_name = "Bulk Ion Temperature" ;
       float Bulk\ Ion\ Velocity\ \(Zonal\)(block, lon, lat, z) ;
           Bulk\ Ion\ Velocity\ \(Zonal\):units = "m/s" ;
           Bulk\ Ion\ Velocity\ \(Zonal\):long_name = "Bulk Ion Velocity (Zonal)" ;
       float Bulk\ Ion\ Velocity\ \(Meridional\)(block, lon, lat, z) ;
           Bulk\ Ion\ Velocity\ \(Meridional\):units = "m/s" ;
           Bulk\ Ion\ Velocity\ \(Meridional\):long_name = "Bulk Ion Velocity (Meridional)" ;
       float Bulk\ Ion\ Velocity\ \(Vertical\)(block, lon, lat, z) ;
           Bulk\ Ion\ Velocity\ \(Vertical\):units = "m/s" ;
           Bulk\ Ion\ Velocity\ \(Vertical\):long_name = "Bulk Ion Velocity (Vertical)" ;
       float Potential(block, lon, lat, z) ;
           Potential:units = "Volts" ;
           Potential:long_name = "Potential" ;
   }

3DBFI_20110320_000000_m0000
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

   netcdf \3DBFI_20110320_000000_m0000 {
   dimensions:
       lon = 22 ;
       lat = 22 ;
       z = 44 ;
       block = UNLIMITED ; // (4 currently)
       time = UNLIMITED ; // (1 currently)
   variables:
       double time(time) ;
       float lon(block, lon, lat, z) ;
           lon:units = "degrees_east" ;
           lon:long_name = "longitude" ;
       float lat(block, lon, lat, z) ;
           lat:units = "degrees_north" ;
           lat:long_name = "latitude" ;
       float z(block, lon, lat, z) ;
           z:units = "m" ;
           z:long_name = "height above mean sea level" ;
       float mlat(block, lon, lat, z) ;
           mlat:units = "degrees" ;
           mlat:long_name = "Magnetic Latitude" ;
       float mlon(block, lon, lat, z) ;
           mlon:units = "degrees" ;
           mlon:long_name = "Magnetic Longitude" ;
       float mlt(block, lon, lat, z) ;
           mlt:units = "hours" ;
           mlt:long_name = "Magnetic Local Time" ;
       float Beast(block, lon, lat, z) ;
           Beast:units = "nT" ;
           Beast:long_name = "Beast" ;
       float Bnorth(block, lon, lat, z) ;
           Bnorth:units = "nT" ;
           Bnorth:long_name = "Bnorth" ;
       float Bvertical(block, lon, lat, z) ;
           Bvertical:units = "nT" ;
           Bvertical:long_name = "Bvertical" ;
   }

