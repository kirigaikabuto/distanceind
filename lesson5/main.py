#input data to 2-dimensional array
# 4 5
# arr=[
# [1 2 3 4 5 ]
# [6 7 8 9 10]
# [11 12 13 14 15]
# [16 17 18 19 20]
# ]
line1 = input().split()
n,m = list(map(int,line1))#[4,5]
arr=[]
for i in range(n):
    line = input().split()
    numbers=list(map(int,line))
    arr.append(numbers)
maxi_all=arr[0][0]
for i in arr:
    #access by column
    # print(i[1])
    maxi=arr[0][0]
    for j in i:
        if j>maxi_all:
            maxi_all = j
        if j>maxi:
            maxi=j
    print(maxi)
    
print(maxi_all)