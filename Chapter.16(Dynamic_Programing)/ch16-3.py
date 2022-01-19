from signal import valid_signals


n = int(input())
t = []
p = []
dp = [0]*(n+1)
for _ in range(n):
    a,b = map(int, input().split())
    t.append(a)
    p.append(b)
value = 0
for i in range(n-1,-1,-1):
    time = t[i]+i
    if time <= n:
        dp[i] = max(value, p[i]+dp[t[i]+i])
        value = dp[i]
    else:
        dp[i] = value
print(value)