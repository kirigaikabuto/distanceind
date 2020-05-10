import random
from mytools import *
arr=[
    [1,2,3,4],
    [5,6,7,8],
    [1,2,3,5]
]
arr2 = list(map(get_max,arr))
print(arr)
print(arr2)