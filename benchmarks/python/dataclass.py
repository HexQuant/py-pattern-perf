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
    from myprofiler.myprofiler import do_profile
    do_profile(
        'Dataclass', (
            ('dataclass', 'func_a'),
            ('namedtuple', 'func_b'),
            ('dictionary', 'func_c'),
            ('class', 'func_d'),
            )
    )