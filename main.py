from ase import atoms
from ase.calculators.gaussian import Gaussian, GaussianOptimizer
from ase.io import *
from ase.optimize import BFGS
from struct_io import *
from calc import *
import os
import matplotlib.pyplot as plt

# Default structure path
struct_path = '/home/erik/RUN/adv_py_course/adpy_proj/structures/'
# Set GAUSS_EXEDIR to your Gaussian path
os.environ["GAUSS_EXEDIR"] = "/home/sw_old/gaussian/g09.d01/intel/bsd:/home/sw_old/gaussian/g09.d01/intel/local:/home/sw_old/gaussian/g09.d01/intel/extras:/home/sw_old/gaussian/g09.d01/intel:/home/sw_old/gaussian/g09.d01/intel/linda8.2/opteron-linux/bin"

# Assigning structure to be treated to 'struct' (type = ase.Atoms)
struct = select_struct(struct_path)
print("\nSuccesfully loaded structure " + struct.get_chemical_formula(mode='hill'))

# Setting up calculation and perform. Files are placed in chosen directory within /calc/
calc, proj_path = calc_set_up()
struct.calc = calc
#print(struct.get_potential_energy())

# Optimization
    # TODO - ask if user wants to optimise structure or calculate vibrations right away
struct = opt(struct,calc)

# Calculation of vibrations, summary of IR frequencies and intensities is printed
struct, spectrum = vib(struct, proj_path)

# spectrum given as a list of lists with frequencies and intensities
plt.plot(spectrum[0], spectrum[1])
