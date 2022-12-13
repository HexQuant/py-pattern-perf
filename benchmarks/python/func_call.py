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
    x = 9000
    for y in range(100):
        result = geom_mean(x, y)

add_lambda = lambda x,y: x+y
mul_lambda = lambda x,y: x*y
geom_mean_labmda = lambda x,y: add_lambda(x,y)/(mul_lambda(x,y)+1)

def func_b():
    x = 9000
    for y in range(100):
        result = geom_mean_labmda(x, y)

def func_c():
    x = 9000
    for y in range(100):
        result = (x+y)/(x*y+1)



if __name__ == '__main__':
    import timeit
    from seaborn import lineplot
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    from tabulate import tabulate

    df = pd.DataFrame()
    number = 1000
    repeat = 100
    df['naive'] = timeit.repeat("func_a()", setup="from __main__ import func_a", repeat=repeat, number=number)
    df['lambda']=timeit.repeat("func_b()", setup="from __main__ import func_b", repeat=repeat, number=number)
    df['inline']=timeit.repeat("func_c()", setup="from __main__ import func_c", repeat=repeat, number=number)
    print(tabulate(df.describe(percentiles=(0.05, 0.50, 0.95))[1:],headers=df.columns, tablefmt='github', floatfmt='.3e'))
    fig = plt.figure()
    ax = df[df.mean().sort_values().index].boxplot()
    ax.set(
        xlabel='Pattern',
        ylabel='Execution time, seconds',
        title = f'Decomposing functions ({repeat=}, {number=})',
        #ylim=(0, None)
        )
    fig.tight_layout()
    fig.savefig('reports/decomposing_functions.png')
