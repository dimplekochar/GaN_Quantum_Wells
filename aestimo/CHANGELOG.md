### v.1.2 (November 6th, 2017)

*	Quaternary alloys (type A_{x}B_{1-x}C_{y}D_{1-y})
*	Added an improved model for modelling conduction band intersubband transitions
*	Added a periodic boundary condition for the Electric field for modelling repeating structures.
*	Small changes were made like to get aestimo to work on python3.4, example files were renamed to be more pythonic etc ...
* 	Code is moved to GitHub.

### v.1.1 (November 8th, 2016)

*    Many small changes and improvements to the intersubband\_optical\_transitions module.
*    Plotting functions now return figure instances; helpful for altering and then saving versions of the plots.
*    Module docstrings have been improved.

### v.1.0 (August 29th, 2014)

*    Many bugfixes,
*    MQW structures ready to be used after the adition of anti-crossing barrier length,
*    A big reorganisation of the Structure and StructureFrom classes. This should make things more self-explanatory for anyone who wants to do something special; normal users shouldn't be affected,
*    Adding a new input parameter 'meff_method' which selects the effective mass functions to use when considering non-parabolicity. This also allows us to not require the material properties in the database to contain unnecessary attributes if we don't want to consider non-parabolicity,
*    Adding functionality to use valence band input files as scripts,
*    Changing file permissions and adding a missing parameter to some of the sample files,
*    Added a utility function to each simulator which carries out the default steps to run a simulation, altered some of the sample files and main.py to use the new function, 
*    Removing aestimo.py cases in main.py and main_interating.py,
*    Get help information is added. Information about obsolete aestimo.py is removed,
*    Adding many tutorials in the form of an ipython notebooks,
*    Allowing aestimo to be used as a package,
*    Moving 'aestimo is starting' message to main section to make using solvers as modules more consistant,
*    A big change to the code to permit the multi-quantum wells calculation,
*    Wurtzite materials are now used in aestimo with,
*    Lots of changes to intersubband optical transitions module. Dielectric constants are now handled more accurately. Although frequency dependent dielectric constants are still not implemented for the matrix model (classical model should be able to handle them),
*    Adding module for calculating dielectric constant and optical absorption of conduction band intersubband transitions,
*    More changes to saving and loading of simulation results,
*    Adding function for loading output data,
*    Adding calculation of fermilevel for non-parabolic subbands,
*    Working on k.p non-parabolicity (Vurgaftman),
*    Adding wavefunction_scalefactor variable to config, controls scaling of wavefunctions on QW diagrams,
*    Many small fixes.

### v.0.9 (November 10th, 2013)

*    Many bugfixes,
*    Speed improvements,
*    Cython code additions,
*    Rewritten VBMAT-V part to use numpy better,
*    Merged conduction and valance band calculations.
*    This is a mostly bugfix version. Code is heavily modified and stabilized with 28 commits.

### v.0.8 (July 7th, 2013)

*    Numpy version is restructured,
*    Input file structure and sample inputs are changed,
*    Non-parabolicity of conduction band is implemented (Numpy version only),
*    Database is changed to a more clear-understable structure,
*    Exchange Interaction Potential is implemented (Numpy version only),
*    Logging with timers and some customizations in config,
*    A sample input to show methods of looping the simulation over a parameter is added,
*    New materials InAs, InP, AlP, GaP and new alloys InGaAs, InGaP, AlInP,
*    Strain included valence band calculation with 3×3 k.p model.
*    Many bugfixes and small corrections,

### v.0.7 (April 27th, 2013)

*    New feature: External electric field,
*    Code is optimized heavily.
*    Numpy version of Aestimo.

### v.0.6 (February, 2013)

*    New configuration properties for outputs and resultviewer.

### v.0.5 (January, 2013)

*    Minor bug fix for calculating electric field.
*    Database support for alloys.

### v.0.4 (November, 2012)

*    Major enhancements.
*    Heterojunction support.
*    Implementing shooting method for Schrödinger eq. (from P. Harrison)

### v.0.3 (October, 2012)

*    Input file support and database support for materials are added.
*    AlAs, GaAs and AlGaAs are added.

### v.0.2.1 (September, 2012)

*    Few minor corrections.
*    Plotting.
*    First documentation draft.

### v.0.2 (June, 2012)

*    Simple Poisson solver for silicon p-n homojunction.

### v.0.1 (March, 2012)

*    Simple electric field calculator for silicon.
