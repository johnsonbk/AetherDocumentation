########
Overview
########

.. important::

   The `CAM Reference Manual <https://www.cesm.ucar.edu/models/cesm1.2/cam/docs/rm5_3/rm.html>`_ 
   is more comprehensive than the current
   `CESM2.X documentation <https://ncar.github.io/CAM/doc/build/html/index.html>`_.
   It even says, "This manual is intended for anyone who plans to get their
   hands dirty modifying CAM code."

   For example, this `CESM1.2 Physics Driver <https://www.cesm.ucar.edu/models/cesm1.2/cam/docs/rm5_3/ch04.html>`_ 
   page in the reference manual doesn't seem to have an analog in the CESM2.X
   documentation.

Nomenclature
============

CAM distinguishes between `Dynamical cores`_ and `Physics packages`_. State 
variables are updated first by the dynamics and then by the physics. Both the
dynamical cores and the physics packages are implemented in a modular fashion
and plug into the model infrastructure using an interface. 

Dynamical cores
---------------

Dynamical cores are numerical methods implemented on specific model grids that
simulate the large scale atmospheric flow. `CAM supports several dynamical
cores <https://www.cesm.ucar.edu/events/wg-meetings/2017/presentations/plenary/lauritzen.pdf>`_
including the:

- EUL (Eulerian spectral-transform)
- SLD (semi-Lagrangian spectral-transform)
- FV (finite-volume)
- SE (spectral-elements)

Physics packages
----------------

Physics packages implement parameterized physical processes within a single
column of the model grid. This functionality is often called a *vertical
solver* within the space weather community.

Kalnay et al. (1989) [1]_ describe eleven rules to ensure physics package
interoperability. Packages should only be responsible for performing a
calculation upon either a single column or a limited section of the model's
state. Other aspects of model integration such as communication,
parallelization, input and output are handled by the support infrastructure
within the model.

These standards allow for modularity and were developed in response to the
difficulty of inserting and comparing physics schemes into a given model.

Coding standards
================

CAM doesn't have a strict set of coding standards because much of its source
code was contributed by the community. However, the UCAR wiki has a `draft of
coding standards for CAM <https://wiki.ucar.edu/display/ccsm/Draft+of+Coding+Standards+for+CAM>`_.
The document nodes that most of the code is preprocessed with Fortran
preprocessor, ``fpp``, which is not officially a part of the Fortran language
standard.

Directory structure
===================

This collection contains pages corresponding to each of the subdirectories in
``cesm/components/cam/src/`` that describes what each of the subdirectories
contains.

- :doc:`/cam/advection`
- :doc:`/cam/atmos_phys`
- :doc:`/cam/chemistry`
- :doc:`/cam/control`
- :doc:`/cam/cpl`
- :doc:`/cam/dynamics`
- :doc:`/cam/ionosphere`
- :doc:`/cam/overview`
- :doc:`/cam/physics`
- :doc:`/cam/unit_drivers`
- :doc:`/cam/utils/`

References
==========

.. [1] Kalnay, E., M. Kanamitsu, J. Pfaendtner, J. Sela, M. Suarez, J. 
       Stackpole, J. Tuccillo, L. Umscheid, and D. Williamson., 1989: Rules for
       Interchange of Physical Parameterizations. Bulletin of the American
       Meteorological Society, 70, 620–622,
       https://journals.ametsoc.org/view/journals/bams/70/6/1520-0477_1989_070_0620_rfiopp_2_0_co_2.xml.
