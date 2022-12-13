
def func_a()->None:
    x:float = 1.0
    for i in range(100):
        x=x+i
        x=x*i
        x=x/10
        x=x-2

def func_b()->None:
    x:float = 1.0
    for i in range(100):
        x+=i
        x*=i
        x/=10
        x-=2

if __name__ == '__main__':
    from myprofiler.myprofiler import do_profile
    do_profile(
        'Compound operators', (
            ('naive', 'func_a'),
            ('compound_ops', 'func_b'),
            ),
    )