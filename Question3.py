#!/usr/bin/env python3
# LAPLACE PROJECT 2019-2020
# MIHAIL KIROV, GWENN JEAN, GASPARD LEVIFVE
# INSA 2019 S5
from generate import *
import matplotlib.pyplot as plt


def count(n, m, criteria):
    """ Count the number of individuals respecting
        the criteria  """

    return sum([1 if element >= criteria else 0 for element in set_integers(n, m)])




def graphe(perturb, n, m, sensitivity, budget, func): # num_pert - list
    """ Plot of the number of perturbations (n) and the average perturbed
        value as well as the the real count"""

    result = func(n, m) # obtaining the real result of the applied function

    fig, ax = plt.subplots(1, figsize=(8, 6))
    fig.suptitle("Average perturbation")
    res_average = list()

    for num_pert in perturb:
        liste_perturb = list()
        for j in range(num_pert):
            error = laplace_noise(sensitivity, budget)
            liste_perturb.append(result + error)

        average = sum(liste_perturb)/num_pert
        res_average.append(average)

    for_plot_result = [result for i in range(len(perturb))]
    plt.plot(perturb, res_average)
    plt.plot(perturb, for_plot_result)
    plt.xscale('log')

    plt.show(block=False)
    plt.pause(5)
    plt.close()


def compare_graph(perturb, n, m, sensitivity, func, budget):
    """ Comparing the the different speed of convergence of the
        average perturbations to the real average result in function of
        different epsilons
    """

    fig, ax = plt.subplots(1, figsize=(8, 6))
    fig.suptitle("Different convergences in function of epsilon")

    result = func(n, m)  # obtaining the real result of the applied function

    for epsilon in budget:
        res_average = list()
        for num_pert in perturb:
            liste_perturb = list()
            for j in range(num_pert):
                error = laplace_noise(sensitivity, epsilon)
                liste_perturb.append(result + error)

            average = sum(liste_perturb)/num_pert
            res_average.append(average)

        for_plot_result = [result for i in range(len(perturb))]
        plt.plot(perturb, res_average)
        plt.plot(perturb, for_plot_result)
        plt.xscale('log')

    plt.show(block=False)
    plt.pause(7)
    plt.close()


if __name__=='__main__' :

    print("Analyse Laplace")
    print("Number of integers greater than 20 in a randomly generated set of 10^3 elements")
    r = count(10 ** 3, 1000, 20)
    print(r)
    print("Average error of 10 perturbations on 10^3 integers between [0-1000]")
    error = 0
    for i in range(10):
        error += laplace_noise(1, 1)  # test mode with 0 0
    print(error/10)

    perturb = [10**i for i in range(1, 7)]
    graphe(perturb, 10**3, 1000, 1, 10**-4, lambda x, y: count(x, y, 10))

    # Generate the convergence graph of the perturbations

    perturb = [i**2 for i in range(1, 200)]
    budget = [0.01, 0.001, 0.0001]
    compare_graph(perturb, 10**3, 1000, 1, lambda x, y: count(x, y, 0), budget)





