from tkinter import S


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp =[]
    arr = list(map(int, input().split()))
    index=0
    for i in range(n):
        dp.append(arr[index:index+m])
        index+=m
    for j in range(1,m):
        for i in range(n):
            if i ==0:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1]) + dp[i][j]
            elif i == n-1:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + dp[i][j]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1], dp[i+1][j-1]) + dp[i][j]
    result = 0
    for i in dp:
        result = max(result, i[m-1])
    print(result)