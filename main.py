from ase import atoms
from ase.calculators.gaussian import Gaussian, GaussianOptimizer
from ase.io import *
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from struct_io import *
from calc import *

# Default structure path
struct_path = '/home/erik/RUN/adv_py_course/adpy_proj/structures/'

# Assigning structure to be treated to 'struct' (type = ase.Atoms)
struct = select_struct(struct_path)
print("Succesfully loaded structure " + struct.get_chemical_formula(mode='hill'))

# Setting up calculation. Files are placed in chosen directory within /calc/
calc = calc_set_up()

struct.calc = calc
