import random
n = int(input())
numbers=[]
for i in range(n):
    num = random.randint(0,20)
    numbers.append(num)
print(numbers)
# print(sorted(numbers))
# 10, 20, 7, 19, 20, 2
# choice=10
for i in range(n):
    choice=numbers[i]
    for j in range(n):
        if choice<numbers[j]:
            tmp  = numbers[i]
            numbers[i]= numbers[j]
            numbers[j]=tmp
print(numbers)


