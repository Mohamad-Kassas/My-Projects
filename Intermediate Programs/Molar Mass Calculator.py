import pandas as pd
import numpy as np
import string

atome_dictionary = {
    "masse_molaire": [1.01, 4, 6.94, 9.01, 10.81, 12.01, 14.01, 16, 19, 20.18, 22.99, 24.31, 26.98, 28.09, 30.97, 32.07,
                      35.45, 39.95, 39.1,
                      40.08, 44.96, 47.88, 50.94, 52, 54.94, 55.85, 58.93, 58.69, 63.55, 65.39, 69.72, 72.63, 74.92,
                      78.97, 79.9, 83.8, 85.47,
                      87.62, 88.91, 91.22, 92.91, 95.95, 98, 101.07, 102.91, 106.42, 107.87, 112.41, 114.82, 118.71,
                      121.76, 127.6, 126.9,
                      131.29, 132.91, 137.33, 138.91, 140.12, 140.91, 144.24, 145, 150.36, 151.97, 157.25, 158.93,
                      162.5, 164.93, 167.26,
                      168.93, 173.04, 175.07, 178.49, 180.95, 183.84, 186.21, 190.23, 192.22, 195.08, 196.97, 200.59,
                      204.38, 207.2, 208.98,
                      209, 210, 222, 223, 226.03, 227.03, 232.04, 231.04, 238.03, 237.05, 244, 243, 247, 247, 251, 252,
                      257, 258, 259, 262, 267,
                      268, 271, 272, 270, 276, 281, 280, 285, 284, 289, 288, 293, 294, 294],
    "numero_atomique": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
                        25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
                        49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72,
                        73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,
                        97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
                        117, 118],
    "nom": ["Hydrogène", "Hélium", "Lithium",
            "Béryllium", "Bore", "Carbone", "Azote", "Oxygène", "Fluor", "Néon", "Sodium", "Magnésium", "Aluminium",
            "Silicium", "Phosphore", "Soufre",
            "Chlore", "Argon", "Potassium", "Calcium", "Scandium", "Titane", "Vanadium", "Chrome", "Manganèse", "Fer",
            "Cobalt", "Nickel", "Cuivre",
            "Zinc", "Gallium", "Germanium", "Arsenic", "Sélénium", "Brome", "Krypton", "Rubidium", "Strontium",
            "Yttrium", "Zirconium", "Niobium",
            "Molybdène", "Technétium", "Ruthénium", "Rhodium", "Palladium", "Argent", "Cadmium", "Indium", "Étain",
            "Antimoine", "Tellure", "Iode",
            "Xénon", "Césium", "Baryum", "Lanthane", "Cérium", "Praséodyme", "Néodyme", "Prométhium", "Samarium",
            "Europium", "Gadolinium", "Terbium",
            "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutécium", "Hafnium", "Tantale", "Tungstène",
            "Rhénium", "Osmium", "Iridium",
            "Platine", "Or", "Mercure", "Thallium", "Plomb", "Bismuth", "Polonium", "Astate", "Radon", "Francium",
            "Radium", "Actinium", "Thorium",
            "Protactinium", "Uranium", "Neptunium", "Plutonium", "Américium", "Curium", "Berkélium", "Californium",
            "Einsteinium", "Fermium", "Mendélévium",
            "Nobélium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnérium",
            "Darmstadtium", "Roentgenium",
            "Copernicium", "Nihonium", "Flérovium", "Moscovium", "Livermorium", "Tennesse", "Organesson"]
}
atoms_df = pd.DataFrame(atome_dictionary, columns=["masse_molaire", "numero_atomique", "nom"],
                        index=["H", "He", "Li", "Be", "B", "C", "N",
                               "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V",
                               "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As",
                               "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd",
                               "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce",
                               "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta",
                               "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi",
                               "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf",
                               "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs",
                               "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"])


def molecule_list_creator():
    global molecule
    molecule = input("Enter the chemical syntax of the molecule: ")
    molecule_list = []
    letter_lower = list(string.ascii_lowercase)
    letters_upper = list(string.ascii_uppercase)
    for i in range(len(molecule)):
        if molecule[i].isupper():
            if i + 1 < len(molecule):
                if molecule[i + 1].isupper() or molecule[i + 1].isnumeric():
                    molecule_list.append(molecule[i])
                if molecule[i + 1].islower():
                    element = molecule[i] + molecule[i + 1]
                    molecule_list.append(element)
            if i + 1 == len(molecule):
                molecule_list.append(molecule[i])
                break
        if molecule[i].isnumeric():
            if i + 1 < len(molecule):
                if molecule[i + 1].isupper():
                    molecule_list.append(molecule[i])
                if molecule[i + 1].isnumeric():
                    number = molecule[i] + molecule[i + 1]
                    molecule_list.append(number)
                if molecule[i - 1].isnumeric():
                    molecule_list.pop(i)
        if i == len(molecule) - 1:
            if molecule[i - 1].isnumeric() and molecule[i - 2].isalpha():
                break
            else:
                if molecule[i].isnumeric():
                    molecule_list.append(molecule[i])
                    if molecule[i - 1].isnumeric():
                        if molecule[i - 2].isupper():
                            molecule_list.pop(i)
                        if molecule[i - 2].islower():
                            molecule_list.pop(i - 1)
                if molecule[i].isupper():
                    molecule_list.append(molecule[i])
    return molecule_list


def molar_mass():
    molecule_list = molecule_list_creator()
    total_mol_mass = 0
    for i in range(len(molecule_list)):
        if molecule_list[i].isalpha():
            mol_mass = atoms_df.loc[molecule_list[i], "masse_molaire"]
        if i != len(molecule_list) - 1:
            if molecule_list[i + 1].isnumeric():
                mol_mass = mol_mass * float(molecule_list[i + 1])
        if molecule_list[i].isnumeric():
            continue
        total_mol_mass = total_mol_mass + mol_mass
    print("The molar mass of " + molecule + ":", round(total_mol_mass, 2), "g/mol")


molar_mass()
