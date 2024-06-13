import numpy as np
import pandas as pan
from timeit import timeit

l = [1, 2, 3, 4, 5]


#for i in l: print(i)

# for e in range(10, 20):
def func1():
    l2 = list(filter(lambda e: e % 3 == 0,  range(10, 20)))
    #l2 = [e*e for e in range(10, 20) if e % 3 == 0]
    print(l2)
    print(f'Lenth of the result: {len(l2)}')
    s = {1, 3, 5, 7, 9}
    s2 = [2, 3, 5, 7, 11]
    s3 = s.intersection(s2)
    print(s3)
def key_func():
    dict1 = {"a": 1, "b": 2, "c": 3}   
    kl = ['a', 'b', 'c', 'd']
    for k in kl:
        print(f"get function gets: {dict1.get(k, 0)}") 

#print(f"func1 took {timeit(func1, number=5)/5}")
#print(f"func1 took {timeit(key_func, number=5)/5}")
#print(len(s))

a1 = np.array((3,3))
a2 = np.full((3, 3), 0.5)
print(a1)
print(a2)