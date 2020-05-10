def print_arr(arr):
    for i in arr:
        print(i,end=" ")
    print()

def get_max(arr):
    maxi=arr[0]
    for i in arr:
        if i>maxi:
            maxi = i
            
    return maxi