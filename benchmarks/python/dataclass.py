from collections import namedtuple
from dataclasses import dataclass


@dataclass(slots=True)
class MyDataClass:
    #__slots__ = 'int_field', 'str_field', 'bool_field', 'float_field'
    int_field: int
    str_field: str
    bool_field: bool
    float_field: float


MyNamedTuple = namedtuple(
    'MyNamedTuple', 'int_field str_field bool_field float_field')

class MyClass:
    __slots__ = 'int_field', 'str_field', 'bool_field', 'float_field'
    def __init__(self,int_field: int, str_field: str, bool_field: bool, float_field: float)->None:
        self.int_field, self.str_field = int_field, str_field
        self.bool_field, self.float_field = bool_field, float_field

def func_a() -> None:
    x = []
    for i in range(10):
        x.append(MyDataClass(9000+i, 'foo', True, (i+2)/2))

    for xx in x:
        a = xx.int_field
        b = xx.float_field


def func_b() -> None:
    x = []
    for i in range(10):
        x.append(MyNamedTuple(9000+i, 'foo', True, (i+2)/2))

    for xx in x:
        a = xx.int_field
        b = xx.float_field


def func_c() -> None:
    x = []
    for i in range(10):
        my_dict = {
            'int_field': 9000+i,
            'str_field': 'foo',
            'bool_field': True,
            'float_field': (i+2)/2
        }
        x.append(my_dict)

    for xx in x:
        a = xx['int_field']
        b = xx['float_field']

def func_d() -> None:
    x = []
    for i in range(10):
        x.append(MyClass(9000+i, 'foo', True, (i+2)/2))

    for xx in x:
        a = xx.int_field
        b = xx.float_field

if __name__ == '__main__':
    import timeit
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    from tabulate import tabulate

    df = pd.DataFrame()
    number = 1000
    repeat = 100
    df['dataclass'] = timeit.repeat("func_a()", setup="from __main__ import func_a", repeat=repeat, number=number)
    df['namedtuple']=timeit.repeat("func_b()", setup="from __main__ import func_b", repeat=repeat, number=number)
    df['dictionary']=timeit.repeat("func_c()", setup="from __main__ import func_c", repeat=repeat, number=number)
    df['class']=timeit.repeat("func_d()", setup="from __main__ import func_d",  repeat=repeat, number=number)
    print(tabulate(df.describe(percentiles=(0.05, 0.50, 0.95))[1:],headers=df.columns, tablefmt='github', floatfmt='.3e'))
    fig = plt.figure()
    ax = df[df.mean().sort_values().index].boxplot()
    ax.set(
        xlabel='Pattern',
        ylabel='Execution time, seconds',
        title = f'dataclass pattern ({repeat=}, {number=})',
        #ylim=(0, None)
        )
    fig.tight_layout()
    fig.savefig('reports/img_1.png')
