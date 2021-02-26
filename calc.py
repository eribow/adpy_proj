from ase.calculators.gaussian import Gaussian, GaussianOptimizer
from ase.vibrations import Vibrations, Infrared

# Function that ask for calculation settings and returns a ase.calculator object
def calc_set_up():

    methods = set(['LSDA','B3LYP','PBE', 'MPW1PW91', 'HF', 'MP2'])
    basis_sets = set(['STO-3G', '3-21G', '6-31G', '6-31+G*', '6-311G',
                    'cc-pVDZ', 'cc-pVTZ', 'cc-pVQZ', 'aug-cc-pVDZ',
                    'aug-cc-pVTZ', 'aug-cc-pVQZ'])

    calc_dir = input("Name folder in which to place calculations (if it doesn't exist within /calc/ it will be created there): ")
    proj_name = input("Name of calculation/project: ")


    # METHODS
    print("Available methods are:")
    for m in methods:
        print(m)

    method = ''
    while not (method in methods):
        method = input("Select method: ")

        if not (method in methods):
            print("method " + method + " doesn't exist, try gain")


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
    # TODO - maybe return several calculators depending on what we need later?
    return Gaussian(mem='4GB',
                    nprocshared='8',
                    label='calc/' + calc_dir + "/" + proj_name,
                    xc=method,
                    basis=basis,
                    scf=['tight','novaracc'],
                    integral='noxctest',
                    freq=''
                    ), 'calc/' + calc_dir

#def calc_pot_energy(struct):
#    return struct.get_potential_energy()

def opt(struct, calc):
    opt = GaussianOptimizer(struct, calc)

    print("\nBeginning optimization...")
    opt.run(opt=['tight','maxcycles=100'])
    print("Optimization completed!")

    return struct

def vib(struct, proj_path):
    #struct.calc = Gaussian(label='calc/' + proj_name + '/freq',
    #                        freq='')
    print("\nBeginning calculation of IR frequencies...")

    struct.calc = Gaussian(mem='4GB',
                    nprocshared='8',
                    label=proj_path + '/vib',
                    )
    #struct.get_potential_energy()
    ir = Infrared(struct)
    ir.clean()
    ir.run()
    ir.write_spectrum('ir_spectra.dat')
    print("Calculation of vibrational frequencies completed!\nPrinting spectrum...")

    return struct, ir.get_spectrum()
