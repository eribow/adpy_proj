from ase.calculators.gaussian import Gaussian, GaussianOptimizer

# Function that ask for calculation settings and returns a ase.calculator object
def calc_set_up():

    functionals = set(['B3LYP','PBE'])
    basis_sets = set(['6-31+G*', '3-21G', '6-31G'])

    calc_dir = input("Name folder in which to place calculations (if it doesn't exist within /calc/ it will be created there): ")
    proj_name = input("Name of calculation/project: ")

    # FUNCTIONALS
    print("As of now, caculations are made using DFT. Available functionals are:")
    for func in functionals:
        print(func)

    func = ''
    while not (func in functionals):
        func = input("Select functional: ")

        if not (func in functionals):
            print("Functional " + func + " doesn't exist, try gain")

    # BASIS SETS
    print("Available basis sets are:")
    for basis in basis_sets:
        print(basis)

    basis = ''
    while not (basis in basis_sets):
        basis = input("Select basis set: ")

        if not (basis in basis_sets):
            print("Basis set " + basis + " doesn't exist, try gain")

    # Returning ase.calculator object with specified settings
    return Gaussian(label='calc/' + calc_dir + "/" + proj_name,
                    xc=func,
                    basis=basis,
                    scf='tight'
                    )
