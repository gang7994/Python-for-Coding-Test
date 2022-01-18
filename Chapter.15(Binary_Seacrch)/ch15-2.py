n = int(input())
arr = list(map(int, input().split()))

def bs(arr,start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return bs(arr,mid+1, end)
    else:
        return bs(arr,start,mid-1)

result = bs(arr,0,n-1)
if result == None:
    print("-1")
else:
    print(result)