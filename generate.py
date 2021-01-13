#!/usr/bin/env python3
# LAPLACE PROJECT 2019-2020
# MIHAIL KIROV, GWENN JEAN, GASPARD LEVIFVE
# INSA 2019 S5

from random import randint
from random import random
import math

TOTAL_BUDGET = 1  # total budget of noise consumption aka total epsilon


def set_integers(n, m):
    """ Generating a random set of
        n integers with a maximum value of m """

    return [randint(0, m) for i in range(n)]


def laplace_noise(sensitivity, budget):
    """ Generating a random laplacian variable(noise)
        in function of the sensitivity and budget parameter
    """

    ecart_type = sensitivity/budget
    x_unif = random() - 1/2  # unifrom variable between -1/2 and 1/2
    sign = -1 if x_unif < 0 else 1
    return -ecart_type*sign*math.log(1 - 2*abs(x_unif))


def consume(sensitivity, budget, importance):
    """ Function generating a noise with a certain ratio from the total
        budget and sensitivity (test for the different
        importance levels of aggregates)
    """

    global TOTAL_BUDGET

    to_consume = importance*budget
    TOTAL_BUDGET -= to_consume
    if TOTAL_BUDGET >= 0:
        return laplace_noise(sensitivity, to_consume)

    return 0



