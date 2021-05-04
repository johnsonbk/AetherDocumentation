##############
Git submodules
##############

Aether's source code relies on a few dependencies in order to run properly:

- Armadillo
- NetCDF
- nlohmann JSON library

Aether manages these dependencies using `git's submodule capability
<https://git-scm.com/book/en/v2/Git-Tools-Submodules>`_. Submodules are their 
own repositories that are contained within a larger repository. Submodules can
nest within other submodules and their contents can be edited and updated.

Verify your version of git
==========================

In order to get started, you will need to verify which version of git you have
installed because git's support for submodules has changed throughout its
various releases. These instructions will work for releases equal to or newer
than git 2.7. In order to verify which version of git you are using, type:

.. code-block::

   git --version

Adding a submodule to a repository
==================================

.. code-block::

   mkdir external
   git submodule add https://github.com/nlohmann/json external/json

Modifying your git config to show the status of submodules
==========================================================

.. code-block::

   git config --global status.submoduleSummary true

Organization of the .gitmodules file
====================================

The submodules are defined in a dot file stored in the root directory of the
repository, ``.gitmodules``.

.. code-block::

   cat .gitsubmodules
   [submodule "external/json"]
       path = external/json
       url = https://github.com/nlohmann/json

Cloning a repository and its submodules
=======================================

.. code-block::

   git clone https://github.com/AetherModel/Aether.git
   cd Aether
   git submodule init 
   git submodule update

Removing a submodule from a repository
======================================

Temporary removal
-----------------

.. code-block::

   git submodule deinit external/json

Permament removal
-----------------

.. code-block::

   git submodule deinit external/json
   git rm external/json
   git commit -m "Removed json submodule"
