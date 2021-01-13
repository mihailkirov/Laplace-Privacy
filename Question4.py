#!/usr/bin/env python3
# LAPLACE PROJECT 2019-2020
# MIHAIL KIROV, GWENN JEAN, GASPARD LEVIFVE
# INSA 2019 S5


from generate import *
import matplotlib.pyplot as plt


def sum_agr(n, m):  # n <- number of individuals, m limit
    """ Generates a list of n elements with values
        b/w 0 and m and returns the sum  of the
        generated set """

    return sum(set_integers(n, m))


def error_average(m, set_size):  # set_size - number of perturbation, m - sensitivity
    """ This function calculates the average value of the sum of the absolute errors sampled
        set_sized times from a laplacian distribution with sensitivity m
    """

    if set_size == 0:
        return 0

    error_tmp = 0
    for _ in range(set_size):
        error_tmp += abs(laplace_noise(m, 10**(-2)))

    return error_tmp/set_size


def sum_and_ratio(set_size, sensitivity):  # sensitivity corresponding to the max value in the set
    """ This function calculates the ration between the average absolute error and the sum
        of all aggregates
    """
    return error_average(sensitivity, set_size)/sum_agr(set_size, sensitivity)


if __name__=='__main__' :

    # Test for the average error

    fig, ax = plt.subplots(1, figsize=(8, 6))
    fig.suptitle("Average error in function of the data-size")
    abcisse, err_moy = list(), list()
    for i in range (2, 8):
         err_moy.append(error_average(1000, 10**i))
         abcisse.append(10**i)

    plt.plot(abcisse, err_moy)
    plt.xscale('log')
    plt.show(block=False)
    plt.pause(5)
    plt.close()

    # COMPUTE THE SUM IN FUNCTION OF THE DATASET SIZE

    abcisse, ordonate = list(), list()
    fig, ax = plt.subplots(1, figsize=(8, 6))
    fig.suptitle("Ration between average error and sum")

    for i in range(2, 7, 2):
        set_size = 10**i
        abcisse.append(set_size)
        ordonate.append(sum_and_ratio(set_size, 1000))

    plt.plot(abcisse, ordonate)
    plt.xscale('log')
    plt.show(block=False)
    plt.pause(5)
    plt.close()



