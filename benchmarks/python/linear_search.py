from numpy import any, ndarray
from numpy.random import randint
from numba import njit
from numba.typed import List as NumbaList

np_vec = randint(0, 9000, size=1000_000)
py_list = np_vec.tolist()
numba_list = NumbaList(py_list)
value = py_list[-1]


def in_search(vec:list, x:int)->bool:
    return x in vec

def for_search(vec:list, x:int)->bool:
    for i in range(len(vec)):
        if vec[i] == x:
            return True
    return False

def foreach_search(vec:list, x:int)->bool:
    for v in vec:
        if v == x:
            return True
    return False

def numpy_any_search(vec:ndarray, x:int)->bool:
    return any(vec==x)

@njit(cache=True)
def numba_in_search(vec:NumbaList, x:int)->bool:
    return x in vec

@njit(cache=True)
def numba_for_search(vec:NumbaList, x:int)->bool:
    for i in range(len(vec)):
        if vec[i] == x:
            return True
    return False

@njit(cache=True)
def numba_foreach_search(vec:NumbaList, x:int)->bool:
    for v in vec:
        if v == x:
            return True
    return False

def func_a()->None:
    in_search(py_list, value)

def func_b()->None:
    for_search(py_list, value)

def func_c()->None:
    foreach_search(py_list, value)

def func_d()->None:
    numpy_any_search(np_vec, value)

def func_e()->None:
    numba_in_search(numba_list, value)

def func_f()->None:
    numba_for_search(numba_list, value)

def func_g()->None:
    numba_foreach_search(numba_list, value)

if __name__ == '__main__':
    import platform

    uname = platform.uname()
    print(f"System: {uname.system} {uname.machine} ({uname.release})")
    print(f"Processor: {uname.processor}")

    from myprofiler.myprofiler import do_profile
    do_profile(
        'Linear search', (
            ('in_statment', 'func_a'),
            ('for_loop', 'func_b'),
            ('foreach_loop', 'func_c'),
            ('numpy_any', 'func_d'),
            ('numba_in_statment', 'func_e'),
            ('numba_for_loop', 'func_f'),
            ('numba_foreach_loop', 'func_g'),
            ),
            number=100
    )