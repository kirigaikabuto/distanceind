arr=[10,12,39,49,5]
n = len(arr)
for i in range(n):
    print("внешний цикл",arr[i])
    for j in range(n):
        print("внутренний цикл",arr[j])