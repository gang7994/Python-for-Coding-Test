import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append([b,1])
    graph[b].append([a,1])
q = [(0,1)]
distance[1] = 0
while q:
    dis, node = heapq.heappop(q)
    if distance[node] < dis:
        continue
    for i in graph[node]:
        cost = dis + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, [cost, i[0]])

max_node = 0
max_distance = 0
result = []
for i in range(1,n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
print(max_node, max_distance, len(result))
        