n , m = map(int, input().split())
arr = list(map(int, input().split()))
result=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]!=arr[j]):
            result+=1
print(result)