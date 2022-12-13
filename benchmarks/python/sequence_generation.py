from collections.abc import Iterator

MAX_ELEMENTS:int = 100

def func_a()->list:
    result = []
    for i in range(MAX_ELEMENTS):
        if i % 2:
            result.append((i+1)*2)
    return result

def func_b()->list:
    return [(i+1)*2 for i in range(MAX_ELEMENTS) if i % 2]


def func_c()->Iterator:
    return ((i+1)*2 for i in range(MAX_ELEMENTS) if i % 2)

# from numpy import ndarray, array

# def func_d()-> ndarray:
#     return array(func_c)

# def func_e()-> ndarray:
#     return array(func_b)

def func_f()->filter:
    return filter(lambda x: x is not None, 
                  map(lambda i: (i+1)*2  if i % 2 else None,
                      range(MAX_ELEMENTS)))

if __name__ == '__main__':
    from myprofiler.myprofiler import do_profile
    do_profile(
        'Sequence generation', (
            ('list forloop', 'func_a'),
            ('list comprehension', 'func_b'),
            ('generator', 'func_c'),
            ('map+filter', 'func_f'),
            )
    )