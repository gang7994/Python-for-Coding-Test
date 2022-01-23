import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

dx = [1,0,-1,0]
dy = [0,1,0,-1]
t = int(input())
for i in range(t):
    n = int(input())
    graph = []
    distance = [[INF]*n for _ in range(n)]
    for j in range(n):
        graph.append(list(map(int, input().split())))
    x,y = 0, 0
    q = [(graph[x][y],x,y)]
    distance[x][y] = graph[x][y]
    
    while q:
        dis , x, y = heapq.heappop(q)
        if distance[x][y] < dis:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  nx < 0 and ny < 0 and nx >= n and ny >= n:
                continue
            cost = dis + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q,(cost, nx, ny))
print(distance[n-1][n-1])