import bisect
n, x = map(int, input().split())
arr = list(map(int, input().split()))

def FindNumber(arr, value):
    left = bisect.bisect_left(arr, value)
    right = bisect.bisect_right(arr, value)
    return right-left

if FindNumber(arr, x) == 0:
    print("-1")
else:
    print(FindNumber(arr,x))