from itertools import combinations

n, m = map(int, input().split())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])

candidates = list(combinations(chicken,m))

def sum_distance(candidate):
    result = 0
    for hx, hy in home:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result+=temp
    return result

result = 1e9

for i in candidates:
    result = min(result, sum_distance(i))
    
print(result)