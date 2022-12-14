import random
from enum import Enum, IntEnum

class Ticker(IntEnum):
    AAPL:int = 143
    MSFT = 257
    GOOG = 95
    AMZN = 91
    TSLA = 157
    NVDA = 176
    TSM = 80
    TCEHY = 41
    META = 122

def match_case(value: Ticker):
    match value:
      case Ticker.AAPL:
        return '000'
      case Ticker.MSFT:
        return '001'
      case Ticker.GOOG:
        return '010'
      case Ticker.AMZN:
        return '011'
      case Ticker.TSLA:
        return '100'
      case Ticker.NVDA:
        return '101'
      case Ticker.TSM:
        return '110'
      case Ticker.TCEHY:
        return '111'
      case Ticker.META:
        return '1000'
      case _:
        return 'NA'

def if_else(value: Ticker):
    if value == Ticker.AAPL:
        return '000'
    elif value == Ticker.MSFT:
        return '001'
    elif value ==  Ticker.GOOG:
        return '010'
    elif value ==  Ticker.AMZN:
        return '011'
    elif value ==  Ticker.TSLA:
        return '100'
    elif value ==  Ticker.NVDA:
        return '101'
    elif value ==  Ticker.TSM:
        return '110'
    elif value ==  Ticker.TCEHY:
        return '111'
    elif value ==  Ticker.META:
        return '1000'
    else:
        return 'NA'

pre_dict = {
    Ticker.AAPL: lambda: '000',
    Ticker.MSFT: lambda: '001',
    Ticker.GOOG: lambda: '010',
    Ticker.AMZN: lambda: '011',
    Ticker.TSLA: lambda: '100',
    Ticker.NVDA: lambda: '101',
    Ticker.TSM: lambda: '110',
    Ticker.TCEHY: lambda: '111',
    Ticker.META: lambda: '1000'
}

def dict_case(dictionary: dict, value: Ticker):
    return dictionary.get(value, lambda: 'NA')()

randomlist = random.sample(range(40, 200), 100)

def func_a()->None:
    for i in randomlist:
        match_case(i)
    
def func_b()->None:
    for i in randomlist:
        if_else(i)

def func_c()->None:
    for i in randomlist:
        dict_case(pre_dict, i)

if __name__ == '__main__':
    from myprofiler.myprofiler import do_profile
    do_profile(
        'Switch case', (
            ('switch_case', 'func_a'),
            ('if_else', 'func_b'),
            ('dict', 'func_c'),
        ),
    )