INF = int(1e9*1e9)
n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b, cost = map(int, input().split())
    if graph[a][b] != INF:
        graph[a][b] = min(graph[a][b], cost)
    else:
        graph[a][b] = cost
for i in range(n+1):
    for j in range(n+1):
        if i==j:
            graph[i][j] = 0
            
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] +graph[k][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] != INF:
            print(graph[i][j],end=' ')
        else:
            print('0',end=' ')
    print()