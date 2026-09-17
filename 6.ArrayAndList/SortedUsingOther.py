import numpy as np
import pandas as pd


def  SortValues(a:list, b:list):
    x = [val for _, val in sorted(zip(b,a))]
    print(x)
    #Using Numpys
    res = [a[i] for i in np.argsort(b)]
    print(res)
    df = pd.DataFrame({'a':a, 'b':b})
    result = df.sort_values('b')['a'].tolist()
    print(result)

a = ['a', 'b', 'c', 'd']
b = [3, 1, 4, 2]
SortValues(a,b)