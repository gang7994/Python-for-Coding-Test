def recursion_bs(arr, target, start, end):
    if start > end:
        return 
    mid = (start+end)//2
    if target > arr[mid]:
        return recursion_bs(arr, target, mid+1, end)
    elif target < arr[mid]:
        return recursion_bs(arr, target, start, mid-1)
    else:
        return mid

def loop_bs(arr, target):
    start = 0
    end = len(arr)-1
    while start < end:
        mid = (start+end)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return 
            

a = [0,2,4,6,8,10,12,14,16,18]

print(recursion_bs(a,2,0,9))
print(loop_bs(a,4))