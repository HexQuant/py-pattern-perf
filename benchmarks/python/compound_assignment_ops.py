
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
    import timeit
    print(timeit.timeit("func_a()", setup="from __main__ import func_a"))
    print(timeit.timeit("func_b()", setup="from __main__ import func_b"))