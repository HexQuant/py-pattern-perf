glob_var = []


def func_a() -> None:
    global glob_var
    glob_var = []


def func_b() -> None:
    global glob_var
    glob_var.append(9000)


if __name__ == '__main__':

    from myprofiler.myprofiler import do_profile
    do_profile(
        'Global var', (
            ('write []', 'func_a'),
            ('append []', 'func_b'),
            ),
    )
