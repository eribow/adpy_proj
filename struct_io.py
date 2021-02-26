from ase.io import *
import glob

def select_struct(struct_path):
    def_man = '0'

    while (def_man != '1') and (def_man != '2'):
        def_man = input("Use default structure path [1] or enter path manually [2] (choose 1 or 2): ")

        if def_man != '1':
            struct_path = input("Enter path to folder containing structures: ")

    print("Available structures are: ")
    struct_list = glob.glob(struct_path + '*xyz')
    for path in struct_list:
        print(path)

    while True:
        struct = input("Select structure to be treated (you can omitt \'.xyz\'): ") + '.xyz'

        try:
            return read(struct_path + struct)

        except:
            print("Error reading structure, try again")
