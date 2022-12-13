glob_var = []


def func_a() -> None:
    global glob_var
    glob_var = []


def func_b() -> None:
    global glob_var
    glob_var.append(9000)


if __name__ == '__main__':
    import timeit
    print(timeit.repeat("func_a()", setup="from __main__ import func_a"))
    print(timeit.repeat("func_b()", setup="from __main__ import func_b"))
