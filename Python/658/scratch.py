def binarySearch(arr,x):
    a, b = 0, len(arr)-1
    # i = (a+b)//2
    while True:
        i = (a+b)//2
        if arr[b] == x:
            return b
        elif arr[i] == x:
            return i
        elif b - a == 1:
            return -1 # x is not in arr
        elif x < arr[i]:
            b = i
        else:
            a = i
        # i = (a+b)//2

print(binarySearch([1,2,3,4,5],3))