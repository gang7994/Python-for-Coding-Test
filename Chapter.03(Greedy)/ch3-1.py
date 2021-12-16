# 거스름돈
coin = [500,100,50,10]
count = 0
n = int(input())
for i in coin:
    count += n // i
    n %= i
    
print(count)