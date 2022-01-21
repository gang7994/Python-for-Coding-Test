n = int(input())
soilder = list(map(int, input().split()))
dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if soilder[i] < soilder[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))