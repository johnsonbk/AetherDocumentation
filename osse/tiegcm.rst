TIEGCM Interface
################

Overview
========

This section documents the code in DARTs interface to the Thermosphere
Ionosphere Electrodynamics General Circulation Model (TIEGCM).

DARTs TIEGCM interface implements current best practices within the code base.

The default TIEGCM state variables listed in ``input.nml`` and their
corresponding DART quantities are as follows:

+----------------+----------------------------------------+
| TIEGCM key     | DART quantity                          |
+================+========================================+
| ``NE``         | ``QTY_ELECTRON_DENSITY``               |
+----------------+----------------------------------------+
| ``OP``         | ``QTY_DENSITY_ION_OP``                 |
+----------------+----------------------------------------+
| ``TI``         | ``QTY_TEMPERATURE_ION``                |
+----------------+----------------------------------------+
| ``TE``         | ``QTY_TEMPERATURE_ELECTRON``           |
+----------------+----------------------------------------+
| ``OP_NM``      | ``QTY_DENSITY_ION_OP``                 |
+----------------+----------------------------------------+
| ``O1``         | ``QTY_ATOMIC_OXYGEN_MIXING_RATIO``     |
+----------------+----------------------------------------+
| ``O2``         | ``QTY_MOLEC_OXYGEN_MIXING_RATIO``      |
+----------------+----------------------------------------+
| ``TN``         | ``QTY_TEMPERATURE``                    |
+----------------+----------------------------------------+
| ``ZG``         | ``QTY_GEOMETRIC_HEIGHT``               |
+----------------+----------------------------------------+
