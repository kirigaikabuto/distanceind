import random
from mytools import *
n = int(input())
numbers=[random.randint(0,20) for i in range(n)]
print_arr(numbers)
mymaxi = get_max(numbers)
print(mymaxi)