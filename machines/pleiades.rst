########
Pleiades
########

Environment overview
====================

`Pleiades' environment <https://www.nas.nasa.gov/hecc/support/kb/hpc-environment-overview_25.html>`_
is protected by secure front ends (SFEs) that users must log in to before 
ssh'ing into either the Pleiades front ends (PFEs) or the Lou front ends
(LFEs).

Logging on and getting onto a PFE
=================================

.. code-block::

   ssh $USER@sfe7.nas.nasa.gov
   [Password]
   [PASSCODE from SecurID]
   ssh pfe
   [Password]

Home and scratch
================

The home directory can be accessed via:

.. code-block::

   /home3/$USER

The scratch directory can be accessed via:

.. code-block::

   /nobackup/$USER

