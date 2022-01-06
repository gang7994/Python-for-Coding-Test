arr = list(map(int, input()))
sum = 0
for i in arr:
    if i == 0 or i == 1 or sum == 0 or sum == 1:
        sum+=i
    else:
        sum*=i
        
print(sum)