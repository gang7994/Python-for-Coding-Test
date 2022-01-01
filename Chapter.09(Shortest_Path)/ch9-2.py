import heapq
INF = int(1e9)
n,m,C = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
distance[0] = 0
for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def telegram(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue
        for i in graph[now]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                heapq.heappush(q,(cost, i[0]))
                distance[i[0]] = cost
      
telegram(C)

count = 0 
for i in range(n+1):
    if distance[i] != 0 and distance[i] != INF:
        count+=1
    if distance[i]==INF:
        distance[i] = 0

print(count, max(distance))

        
'''입력값
6 11 2
1 2 2 
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
'''출력값
4 5
'''