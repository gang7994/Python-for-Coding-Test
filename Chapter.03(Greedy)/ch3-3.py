n, m = map(int, input().split())
result=0
for i in range(n):
    card = list(map(int, input().split()))
    temp = min(card)
    result = max(temp, result)
print(result)

