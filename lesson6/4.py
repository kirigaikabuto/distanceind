# 3
# yerassyl 22
# kirito 30
# ivan 40
n = int(input())
arr=[]
for i in range(n):
    line = input()
    parts = line.split(' ') 
    d={}
    d['name']=parts[0]
    d['age']=int(parts[1])
    arr.append(d)

maxi=arr[0]['age']
person={}
for i in arr:
    if i['age']>maxi:
        maxi = i['age']
        person = i
print(person)