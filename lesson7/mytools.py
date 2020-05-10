def print_arr(arr):
    for i in arr:
        print(i)
 

def get_max(arr):
    maxi=arr[0]
    for i in arr:
        if i>maxi:
            maxi = i

    return maxi
def avg_arr(arr):
    s = 0
    for i in arr:
        s += i
    s /= len(arr)
    return s
    