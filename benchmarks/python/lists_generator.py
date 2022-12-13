

MAX_ELEMENTS = 100

def func_a()->list:
    result = []
    for i in range(MAX_ELEMENTS):
        if i % 2:
            result.append((i+1)*2)
    return result

def func_b()->list:
    return [(i+1)*2 for i in range(MAX_ELEMENTS) if i % 2]


def func_c()->list:
    return ((i+1)*2 for i in range(MAX_ELEMENTS) if i % 2)

def func_cc()->list:
    for i in range(MAX_ELEMENTS):
        if i % 2:
            yield (i+1)*2

from numpy import ndarray, array

def func_d()-> ndarray:
    return array(func_c)

def func_e()-> ndarray:
    return array(func_b)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("func_a()", setup="from __main__ import func_a"))
    print(timeit.timeit("func_b()", setup="from __main__ import func_b"))
    print(timeit.timeit("func_c()", setup="from __main__ import func_c"))
    print(timeit.timeit("func_cc()", setup="from __main__ import func_cc"))
    print(timeit.timeit("func_d()", setup="from __main__ import func_d"))
    print(timeit.timeit("func_e()", setup="from __main__ import func_e"))