n, m, k = map(int, input().split())
list = list(map(int, input().split()))
list.sort()
first = list[n-1]
second = list[n-2]
result = int(m/(k+1) * (first*k+second))
print(result)
    