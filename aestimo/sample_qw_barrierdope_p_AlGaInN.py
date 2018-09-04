#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------
# Input File Description:  Barrier doped AlGaAs/GaAs heterostructure.
# -------------------------------------------------------------------
# ----------------
# GENERAL SETTINGS
# ----------------

# TEMPERATURE
T = 300.0 #Kelvin

# COMPUTATIONAL SCHEME
# 0: Schrodinger
# 1: Schrodinger + nonparabolicity
# 2: Schrodinger-Poisson
# 3: Schrodinger-Poisson with nonparabolicity
# 4: Schrodinger-Exchange interaction
# 5: Schrodinger-Poisson + Exchange interaction
# 6: Schrodinger-Poisson + Exchange interaction with nonparabolicity
computation_scheme = 2

# Non-parabolic effective mass function
# 0: no energy dependence
# 1: Nelson's effective 2-band model
# 2: k.p model from Vurgaftman's 2001 paper
meff_method = 2

# Non-parabolic Dispersion Calculations for Fermi-Dirac
fermi_np_scheme = True

# QUANTUM
# Total subband number to be calculated for electrons
subnumber_h = 4
subnumber_e = 1
# APPLIED ELECTRIC FIELD
Fapplied = 0.00#/50e-9 # (V/m)

# --------------------------------
# REGIONAL SETTINGS FOR SIMULATION
# --------------------------------

# GRID
# For 1D, z-axis is choosen
gridfactor = 0.2 #nm
maxgridpoints = 200000 #for controlling the size
mat_type='Wurtzite'
# REGIONS
# Region input is a two-dimensional list input.
# An example:
# Si p-n diode. Firstly lets picturize the regional input.
#         | Thickness (nm) | Material | Alloy fraction x|Alloy fraction y| Doping(cm^-3) | n or p type |
# Layer 0 |      250.0     |   Si     |      0         |      0         |      1e16      |     n       |
# Layer 1 |      250.0     |   Si     |      0         |      0         |      1e16      |     p       |
#
# To input this list in Gallium, we use lists as:
material =[[ 1000.0, 'GaAs', 0.0, 1e20, 'n'],
            [ 400.0, 'GaAs', 0.0, 5e18, 'n'],
            [ 10.0, 'AlGaAs', 0, 5e18, 'n'],
	    [ 10.0, 'AlGaAs', 0.52, 3e19, 'n'],
	    [ 1.5, 'AlAs', 0, 0, 'n'],
	    [ 1.0, 'GaAs', 0, 0, 'n'],
	    [ 1.75, 'AlGaAs', 0.85, 7e13, 'n'],
	    [ 1.5, 'AlAs', 0, 0, 'n'],
 	    [ 1.5, 'AlAs', 0, 0, 'n'],
	    [ 1.0, 'GaAs', 0, 0, 'n'],
	    [ 1.75, 'AlGaAs', 0.85, 7e13, 'n'],
	    [ 1.5, 'AlAs', 0, 0, 'n'],
 	    [ 1.5, 'AlAs', 0, 0, 'n'],
	    [ 1.0, 'GaAs', 0, 0, 'n'],
	    [ 1.75, 'AlGaAs', 0.85, 7e13, 'n'],
	    [ 1.5, 'AlAs', 0, 0, 'n'],
 	    [ 1.5, 'AlAs', 0, 0, 'n'],
	    [ 1.0, 'GaAs', 0, 0, 'n'],
	    [ 1.75, 'AlGaAS', 0.85, 7e13, 'n'],
	    [ 1.5, 'AlAs', 0, 0, 'n'],
	    [ 10.0, 'AlGaAs', 0.52, 3e19, 'n'],
	    [ 10.0, 'AlGaAs', 0, 5e18, 'n'],
	    [ 400.0, 'GaAs', 0.0, 5e18, 'n'],
	    [ 1000.0, 'GaAs', 0.0, 1e20, 'n']
  ]
#This is accourding to interpolated Vegard’s law for quaternary ABxCyD1-x-y=NGaxAlyIn1-x-y

if __name__ == "__main__": #this code allows you to run the input file directly
    input_obj = vars()
    import aestimo_eh as aestimo
    aestimo.run_aestimo(input_obj)
