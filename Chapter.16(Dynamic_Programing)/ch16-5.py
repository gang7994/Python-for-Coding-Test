n = int(input())
dp = [0]*n
dp[0] = 1
i2 = i3 = i5 = 0
p2, p3, p5 = 2, 3, 5
for i in range(1,n):
    dp[i] = min(p2,p3,p5)
    if dp[i]==p2:
        i2+=1
        p2 = dp[i2]*2
    if dp[i]==p3:
        i3+=1
        p3 = dp[i3]*3
    if dp[i]==p5:
        i5+=1
        p5 = dp[i5]*5
print(dp)