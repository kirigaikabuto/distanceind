import random
n = int(input())
numbers=[]
for i in range(n):
    num = random.randint(0,20)
    numbers.append(num)
mini = numbers[0]
# 1 2 3 4 5
# 0 1 2 3 4
# n = 5
#         n-1
print(numbers)
for i in range(n):
    if numbers[i]<mini:
        mini = numbers[i]

print(mini)