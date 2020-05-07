import random
n = int(input())
# arr=[]
# 
# for i in range(n):
#     arr.append(random.randint(0,20))
arr=[random.randint(0,20) for i in range(n)]
print(arr)
maxi=arr[0]
maxi_index=0
for i in range(n):
    if arr[i]>maxi:
        maxi = arr[i]
        maxi_index=i
print(maxi)
print(maxi_index)
# index_maxi = arr.index(maxi)
#print(index_maxi)