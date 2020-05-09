#3
# yerassyl 22
# kirito 30
# ivan 40
n = int(input())#3
arr=[]
for i in range(n):
    name = input()
    d={}
    d['name']=name
    arr.append(d)

for i in arr:
    print(i['name'])