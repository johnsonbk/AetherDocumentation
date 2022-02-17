###############
Installing CESM
###############

Community Earth System Model (CESM) installation instructions are available via
the `README <https://github.com/ESCOMP/CESM>`_ on the GitHub repository. The
cube sphere grid is available as of CESM2.2.0.

.. note::

   svn isn't installed on the pfe nodes, thus the ``checkout_externals`` script
   fails because it is needed to download ``CESM/components/cam/chem_proc``.
   To get around this issue, download CESM on a laptop or Cheyenne, tar the
   resulting file and transfer it to Pleiades.


Download CESM on a laptop or Cheyenne
=====================================

.. code-block::

   cd <installation_directory>
   git clone https://github.com/ESCOMP/CESM.git cesm2_2_0
   cd cesm2_2_0
   git checkout release-cesm2.2.0
   ./manage_externals/checkout_externals

Log on to a pfe node
====================

.. code-block::

   cd /nobackup/$USER
   sftp <user>@data-access.ucar.edu
   get /glade/work/$USER/CESM.tar.gz
   exit
   tar -xvf CESM.tar.gz 
   
