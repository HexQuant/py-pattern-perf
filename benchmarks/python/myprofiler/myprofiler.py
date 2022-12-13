import timeit
#import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

def do_profile(description:str, funcs:tuple, repeat:int=100, number:int=1000):

    df = pd.DataFrame()
    for name, func in funcs:
        df[name] = timeit.repeat(f'{func}()', setup=f'from __main__ import {func}', repeat=repeat, number=number)

    fig = plt.figure()
    if len(funcs)>4:
        x_rot = 30
    else:
        x_rot = 0
    ax = df[df.mean().sort_values().index].boxplot(rot=x_rot)
    ax.grid(linestyle='--', linewidth=0.5)
    ax.set(
        xlabel='Pattern',
        ylabel='Execution time, seconds',
        title = f'{description} ({repeat=}, {number=})',
        #yscale='log'
        #ylim=(0, None)
        )
    fig.tight_layout()
    unify_desc = description.lower().replace(' ', '_')
    fig.savefig(f'reports/{unify_desc}.png')

    df = df.describe(percentiles=(0.05, 0.50, 0.95))[1:].transpose().sort_values('mean')
    with open(f'reports/{unify_desc}.txt', 'w') as txt_file:
        txt_file.write(tabulate(df,headers=df.columns, tablefmt='github', floatfmt='.2e'))