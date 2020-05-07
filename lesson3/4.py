#получение элементов без повторения
arr=[1,1,3,2,1,3,4,3,4]
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)