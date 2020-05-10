import random
def print_arr(arr):
    for i in arr:
        print(i,end=" ")
    print()
n = int(input())
numbers=[random.randint(0,20) for i in range(n)]
print_arr(numbers)