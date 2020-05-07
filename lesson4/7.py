# 3 4
# 1 2 3 4 
# 5 6 7 8
# 9 10 11 12
import random
n,m = input().split()#3 4
n = int(n)
m = int(m)
arr=[]
for i in range(n):
    for j in range(m):
        arr[i][j]=random.randint(0,20)
sumi=0
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()
for i in range(n):
    for j in range(m):
        sumi=sumi+arr[i][j]
