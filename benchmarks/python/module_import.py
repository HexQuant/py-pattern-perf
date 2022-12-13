# Importing specific name instead of namespace

import math
from math import sqrt

MAX_ELEMENT:int = 100

def func_a() -> list:
    return [math.sqrt(x) for x in range(MAX_ELEMENT)]

def func_b() -> list:
    return [sqrt(x) for x in range(MAX_ELEMENT)]

import numpy as np
from numpy import ndarray, sqrt as np_sqrt
from numpy.random import random


def func_numpy_a() -> np.ndarray:
    x = np.random.random(MAX_ELEMENT)
    return np.sqrt(x)

def func_numpy_b() -> ndarray:
    x = random(MAX_ELEMENT)
    return np_sqrt(x)


if __name__ == '__main__':

    from myprofiler.myprofiler import do_profile
    do_profile(
        'Module imports', (
            ('indirect', 'func_a'),
            ('direct', 'func_b'),
            )
    )
    #print(timeit.timeit("func_numpy_a()", setup="from __main__ import func_numpy_a"))
    #print(timeit.timeit("func_numpy_b()", setup="from __main__ import func_numpy_b"))
