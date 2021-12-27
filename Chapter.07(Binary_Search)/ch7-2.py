n, m = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = max(arr)-1

while start <= end:
    sum = 0
    mid = (start+end)//2
    for i in arr:
        if (i-mid) > 0:
            sum+=(i-mid)
    if(sum == m):
        print(mid)
        break
    elif(sum > m):
        start = mid+1
    else:
        end = mid-1
