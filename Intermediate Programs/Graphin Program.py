import numpy as np
import matplotlib.pyplot as plt


def graphique(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    plt.grid()

nb_ligne = int(input("How many lines are there: "))

def plusieurs_ligne(nb_ligne):

    formules = []
    starting_value = int(input("Enter starting x value: "))
    ending_value = int(input("Enter final x value: "))
    x_range = np.arange(starting_value, ending_value + 1)
    n = len(x_range)
    horizontal_lines = int(input("How many horizontal lines are there: "))
    vertical_lines = int(input("How many vertical lines are there: "))
    formula_lines = nb_ligne - (horizontal_lines + vertical_lines)
    if horizontal_lines > 0:
        for a in range(horizontal_lines):
            number_horizontal_line = int(input("Enter the horizontal line constant number: "))
            plt.axhline(y=number_horizontal_line)
    if vertical_lines > 0:
        for b in range(vertical_lines):
            number_vertical_lines = int(input("Enter the vertical line constant number: "))
            plt.axvline(x=number_vertical_lines)
    for i in range(formula_lines):
        formule = str(input("Enter the formula of line:"))
        formules.append(formule)
    for j in range(len(formules)):
        formula = formules[j]
        graphique(formula, x_range)
    plt.grid()
    plt.show()

plusieurs_ligne(nb_ligne)
