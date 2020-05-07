import random
n = int(input())
numbers=[]
for i in range(n):
    num = random.randint(0,20)
    numbers.append(num)
print(numbers)
mini=numbers[0]
for i in range(n):
    if numbers[i]<mini:
        mini = numbers[i]
second_mini=numbers[1]
if mini != numbers[0]:
    second_mini = numbers[0]

for i in range(n):
    if numbers[i]<second_mini and numbers[i]!=mini:
        second_mini = numbers[i]
print(mini,second_mini)