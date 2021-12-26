from collections import deque
from typing import Mapping
n, m = map(int, input().split())
mapinfo = []
for i in range(n):
    mapinfo.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_x >=n or new_y < 0 or new_y >=m:
                continue
            if mapinfo[new_x][new_y] == 0:
                continue
            if mapinfo[new_x][new_y] == 1:
                queue.append((new_x,new_y))
                mapinfo[new_x][new_y] = mapinfo[x][y]+1
    return mapinfo[n-1][m-1]

print(bfs(0,0))
    