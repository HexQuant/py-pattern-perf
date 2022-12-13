#from numba import jit

#@jit(nopython=True, cache=True)
def add(x: float, y: float) -> float:
    return x+y


#@jit(nopython=True, cache=True)
def mul(x: float, y: float) -> float:
    return x*y


#@jit(nopython=True, cache=True)
def geom_mean(x: float, y: float) -> float:
    return add(x, y)/(mul(x, y)+1)


#@jit(nopython=True, cache=True)
def func_a():
    x:float = 9000
    for y in range(100):
        result = geom_mean(x, y)

add_lambda = lambda x,y: x+y
mul_lambda = lambda x,y: x*y
geom_mean_labmda = lambda x,y: add_lambda(x,y)/(mul_lambda(x,y)+1)

def func_b():
    x:float = 9000
    for y in range(100):
        result = geom_mean_labmda(x, y)

def func_c():
    x:float = 9000
    for y in range(100):
        result = (x+y)/(x*y+1)

from numpy import ndarray, arange

def func_d()->ndarray:
    x:float = 9000
    y = arange(100)
    result = (x+y)/(x*y+1)
    


if __name__ == '__main__':
    from myprofiler.myprofiler import do_profile
    do_profile(
        'Decomposing functions', (
            ('naive', 'func_a'),
            ('lambda', 'func_b'),
            ('inline', 'func_c'),
            ('numpy', 'func_d'),
            )
    )