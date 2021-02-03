##################
Verification tests
##################

Verification tests determine whether a model does what it is designed to do.
Aether is verified by constructing unit tests and integration tests for the
model’s functions during the development process, implementing a structured
walk-through policy for new model modules, comparing both intermediate and
final simulation results to analytic results, and using a range of input
combinations that are both typical and atypical.

There are many challenges in performing these different verification tests,
especially for models of large systems. However, the benefits, which include
but are not limited to catching bugs during software development and providing
users with information on appropriate input ranges, are significant.

Unit tests are run on a predetermined schedule to determine whether mistakes
have been made in committed code, with reports being sent to core developers.

One example of a commonly used unit test is the Sod shocktube, used to verify
the performance of hydrodynamic solvers in computational fluid dynamics codes.

This particular problem has an analytical solution and is thus highly useful
for verification of the numerical implementation. Variations of this problem
can be used to test each dimension in the code separately. Similar higher
dimensional versions of this test, such as the blast wave, can also be used for
verification.