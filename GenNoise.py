#!/usr/bin/env python3
# LAPLACE PROJECT 2019-2020
# MIHAIL KIROV, GWENN JEAN, GASPARD LEVIFVE
# INSA 2019 S5

from generate import *
import matplotlib.pyplot as plt


def histogramme(n, sensitivity):
    """ Plot the histogramme generated from the
        Laplace distribution in TEST MODE
    """

    return [laplace_noise(sensitivity, TOTAL_BUDGET) for _ in range(n)]


if __name__ == '__main__':
    print("Test for Laplace implementation - test mode (using TOTAL_BUDGET)")

    values_laplace = histogramme(2*10**4, 100)
    plt.hist(values_laplace, bins=100)
    plt.show()
