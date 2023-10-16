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

