import sys
n = int(input())
n_arr = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_arr = list(map(int, sys.stdin.readline().split()))

def bs(arr, target, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    if target == arr[mid]:
        return 1
    elif target < arr[mid]:
        return bs(arr, target, start, mid-1)
    else:
        return bs(arr, target, mid+1, end)

n_arr.sort()

for i in m_arr:
    if(bs(n_arr, i, 0, len(n_arr)-1)):
        print('yes',end=' ')
    else:
        print('no',end=' ')