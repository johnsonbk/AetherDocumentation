############################
reStructuredText Style Guide
############################

This page contains example reStructuredText syntax including title headers,
citations, links, code snippets, tables, and quotes.

#. `Major Title`_

   #. `Minor Title`_
   
      #. `Micro Title`_
         
#. `Link Examples`_

   #. `Full Citations in Footnotes`_
   
#. `Useful Syntax`_

   #. `Blockquotes`_
   #. `Definition Lists`_
   #. `Field Lists`_

#. `Code Examples`_
#. `Nested Lists and Inline Literals`_
#. `Bullet List`_
#. `Tables`_
#. `Citations`_

Major Title
===========

Minor Title
-----------

Micro Title
~~~~~~~~~~~

Link Examples
=============

- `Working link`_ will take us to the paragraph that begins with,
  "This link target works."

Headers are also link targets by default. See, for example, how this makes a
link to the `useful syntax`_ section even though the header is capitalized and
this link is not.

Links to external websites, such as the `University of Michigan
<https://umich.edu>`__, are easily accomodated using < > to contain the link
and double underscores at the end of the link syntax.


Full Citations in Footnotes
---------------------------

The Lorenz (1963) [1]_ model is specified by a set of three ordinary
differential equations. The Lorenz (1996) [2]_ model is more complex. The
transition line below separates this paragraph from the two paragraphs below.

------------

.. _`Working link`:

This *link target* works. It works because there is a new line separating the
link target and the text. It is often the case when using reStructuredText that
proper syntax includes a new line to delineate the parts of a particular
structure.

Useful Syntax
=============

Blockquotes
-----------

Long sections of quoted text can be included simply by indenting the paragraph.
Blockquotes can also be nested. Here, we quote from Holton and Hakim (2013)
[3]_:

    A problem with the traditional form of the omega equation is that there
    exists significant cancellation between the two right-side terms. To expose
    this cancellation and develop two different forms of the omega equation, we
    need to expand the right side of (6.42). This involves taking the gradient
    of vector products, for which vector notation is not well suited.

        Just as we use vector notation to simplify mathematical manipulations
        when scalar notation becomes cumbersome, it is often prudent to move to
        *indicial notation* for situations where vector notation becomes
        awkward.
        
Definition Lists
----------------

These lists can be used to introduce terms to the reader.

Forward Operator
  A routine that interpolates values from the model grid to the observation
  location.

Observation Converter
  A program that converts observations from other formats into obs_seq format.
        
Field Lists
-----------

Field lists can be used for describing properties of a model.

:Model: Aether
:Grid: Cube sphere

Code Examples
=============

reStructuredText recognizes C syntax and highlights it appropriately:

.. code-block:: c

    #include <stdio.h>
    int main() {
        printf("Hello, World!");
        return 0;
    }

Syntax highlighting also works in other languages that we might use for scripting such as bash:

.. code-block:: bash

  #!/bin/bash

  for a in `seq 1 10`; do
      echo "$a/10 to Exit." 
      sleep 1;
  done
  
  echo "We are done bashing" 

or python:

.. code-block:: python

  #!/usr/bin/env python
  
  def save(obj):
      return (obj.__class__, obj.__dict__)

  def load(cls, attributes):
      obj = cls.__new__(cls)
      obj.__dict__.update(attributes)
      return obj

Nested Lists and Inline Literals
================================

Directories such as ``Aether/src/bfield.cpp`` or even commands such as ``grep
-Rl dipole ./`` can be called out within a paragraph using what are known as
"inline literals" -- just wrap the desired text by two backticks.

#. Multiple commands can be stacked to instruct users to do several commands at
   once, even a list element:

   ``git clone https://github.com/AetherModel/Aether.git``
  
   ``cd Aether``

#. Here the list continues even after we include three lines of commands.
#. And we have a third list element.

Even more complicated list structures are possible by using spaces to indent
the nested list to the same character column as the content of the outer list.

#. First element in outer list
#. Second element in outer list

   #. First element in nested list is indented by three spaces and separated
      from the outer list by a new line.
   #. Second element in nested list is also indented by three spaces.
   
#. Third element in outer list is not indented but is separated from the nested
   list by a new line.

Bullet List
===========

- Bullet lists are easy to make
- Just make sure there is a new line before and after the list

Tables
======

Complex tables are straightforward to make. See here that the first row of
table data after the table header has only one column instead of three.

+------+--------------------------------+-----------------------------------+
| year | month/day of first,middle,last | obs_seq #### of first,middle,last |
+======+================================+===================================+
| Include GPS when it becomes available?                                    |
+------+--------------------------------+-----------------------------------+
| 2006 |  1/ 1, 1/16, 1/31              | 2954 - 2969 - 2984                |
+------+--------------------------------+-----------------------------------+
| 2006 |  2/ 1, 2/16, 2/28              | 2985 - 3000 - 3012                |
+------+--------------------------------+-----------------------------------+
| 2006 |  3/ 1, 3/16, 3/31              | 3013 - 3028 - 3043                |
+------+--------------------------------+-----------------------------------+
| 2006 |  4/ 1, 4/16, 4/30              | 3044 - 3059 - 3073                |
+------+--------------------------------+-----------------------------------+
| 2006 |  5/ 1, 5/16, 5/31              | 3074 - 3089 - 3104                |
+------+--------------------------------+-----------------------------------+
| 2006 |  6/ 1, 6/16, 6/30              | 3105 - 3120 - 3134                |
+------+--------------------------------+-----------------------------------+
| 2006 |  7/ 1, 7/16, 7/31              | 3135 - 3150 - 3165                |
+------+--------------------------------+-----------------------------------+
| 2006 |  8/ 1, 8/16, 8/31              | 3166 - 3181 - 3196                |
+------+--------------------------------+-----------------------------------+
| 2006 |  9/ 1, 9/16, 9/30              | 3197 - 3212 - 3226                |
+------+--------------------------------+-----------------------------------+
| 2006 |  10/ 1, 10/16, 10/31           | 3227 - 3242 - 3257                |
+------+--------------------------------+-----------------------------------+
| 2006 |  11/ 1, 11/16, 11/30           | 3258 - 3273 - 3287                |
+------+--------------------------------+-----------------------------------+
| 2006 |  12/ 1, 12/16, 12/31           | 3288 - 3303 - 3318                |
+------+--------------------------------+-----------------------------------+

.. table:: Demonstration of simple table syntax.

   ===== ==== ====== =======
   Right Left Center Default
   ===== ==== ====== =======
   12    12   12     12
   123   123  123    123
   1     1    1      1
   ===== ==== ====== =======

Citations
=========

Clicking on the number that denotes each citation links back to its original
mention within the text.

.. [1] Lorenz, Edward N. (1963) “Deterministic Nonperiodic Flow.” *Journal of the Atmospheric Sciences* **20** (2): 130–141.
.. [2] Lorenz, Edward N. (1996) “Predictability – A problem partly solved.” *Seminar on Predictability* **I**: ECMWF.
.. [3] Holton, James R. and Gregory J. Hakim (2013) *An Introduction to Dynamic Meteorology.* Fifth Edition, 552 pages. Academic Press, San Diego, USA. 
