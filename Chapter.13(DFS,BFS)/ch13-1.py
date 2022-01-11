from collections import deque
from typing import Deque

n,m,k,x = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    
distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for i in graph[now]:
        if distance[i] == -1:
            distance[i] = distance[now] + 1
            q.append(i)
answer = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        answer = True

if not answer:
    print('-1')