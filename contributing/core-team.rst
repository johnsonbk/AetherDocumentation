#########
Core Team
#########

While Aether is an open-source project, its development is lead by a core team
of scientists.

Team members
============

**Aaron Ridley** has significant experience developing models and teaching
students. He has worked on porting the TIEGCM to the Linux architecture and
coupling it to a global MHD code. He rewrote the Assimilative Mapping of
Ionospheric Electrodynamics technique, developed an ionospheric electrodynamics
solver, helped to develop the Space Weather Modeling Framework, developed GITM,
helped to develop a state-of-the-art orbit propagator for determining the
probability of collisions, and is currently coupling GITM to the SAMI3 model of
the ionosphere. He teaches engineering and science classes at every level.
Prof. Ridley manages the effort to develop Aether and the supporting education
program. He leads team meetings, helps to develop the architecture of Aether
(including core model, UQ, DA, and OSSE support), leads the development and
gathering of educational resources including the school lesson planning, and
helps with community support.

**Jeffrey Anderson** is a senior scientist at the National Center for
Atmospheric Research where he leads the Data Assimilation Research Section. He
is the lead architect of Data Assimilation Research Testbed, including its
application to large models on high-performance computing. He has extensive
experience in developing ensemble data assimilation algorithms and applying
them to earth system models and observations. Dr. Anderson has experience
applying DART to upper atmosphere and space weather models including GITM,
TIEGCM, Open-GGCM, and WACCM-X and to models that used the cubed-sphere grid
like CAM-SE. He was the lead developer of an earlier version of the GFDL
atmospheric prediction system and the original developer of the GFDL Flexible
Modeling System, a software system for efficient model development.

**Jared Bell** is a planetary atmospheres modeler at GSFC. He has modified the
Earth version of GITM to work at Titan, and has helped to develop the Mars
version of GITM. He has upgraded the time stepping in GITM to be 4th order,
the vertical boundary conditions to be 4th order, and the vertical solver from
a Rusanov-type to the AUSM+-up solver. He is currently working on an oblated
spheroid version of GITM, allowing the radius to the lower boundary to vary as
a function of latitude, so that fast rotating planets, such as Jupiter and
Saturn, can be simulated. His role on the Aether team is to support the model
development, specifically the solvers and the grid system, and its application.

**Alex Glocer** has extensive experience developing and coupling models of the
space environment. He is the primary developer of the Polar Wind Outflow Model
having expanded it from a single field line code to a global code and coupling
it to a global magnetosphere model. He further expanded PWOM to a combined
fluid-kinetic model, and worked on the development of the multi- fluid MHD
BATS-R-US magnetosphere model. He contributes to the development of ring
current and radiation belt models and their coupling with the global
magnetosphere. His role on the Aether team is to support the model development
and application.

**Angeline Burrell** has extensive experience developing scientific programs in
collaborative environments. She is actively working on model validation efforts
at NRL, and is working to create a score card that can be used to track the
global and regional improvement of ionospheric models. Her role will include
supporting the model development by performing code reviews, creating tools for
model validation, validating model results against publicly available data, and
providing community support.

**Meghan Burleigh** is an early career scientist and has experience developing
ionospheric models. She created GEMINI-TIA, a local scale, multi-fluid model
designed for the high-latitude ionosphere. In addition, she is working on
incorporating 2-way coupling of GITM to the SWMF to facilitate self-consistent
physics. She is developing a new course at UM titled “Programming Practices for
Scientists”, with Qusai Al Shidi, that focuses on teaching students good coding
practices, including methods that promote collaboration and facilitate version
control. Her role on the Aether team includes assisting with the development of
the architecture of Aether, contributing to educational resources, teaching at
the coding school, and providing community support.

**Qusai Al Shidi** is an early career scientist with experience in both space
physics and computer science, having developed a solar chromosphere model from
scratch. The model is a two-fluid collisional MHD model. Ionosphere and
chromosphere MHD models are usually presented together since they share the
same multi-fluid and collisional physics. He is currently working on studying
the energy transfer of ICME's into storms by running multi-scale Space Weather
Modeling Framework simulations of the Sun-Earth system, from solar wind to
ionosphere. His role will include Aether development and developing software
standards for Aether and its teaching.

**Ben Johnson** is an early career scientist who works with the NCAR
software engineer and Jeff Anderson to develop DART interfaces to Aether that
will support the science requirements of the project. He assists software
engineer in implementing these interfaces, provide scientific expertise in the
evaluation of both OSSE and real-data tests of DART/Aether, and lead the
implementation of enhanced documentation and tutorial material for ensemble
data assimilation.