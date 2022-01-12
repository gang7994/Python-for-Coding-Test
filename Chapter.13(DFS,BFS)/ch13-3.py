from collections import deque


n, k =  map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
virus_list = []    
s, tar_x, tar_y = map(int, input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            virus_list.append((data[i][j], 0, i, j))
            
virus_list.sort()
q = deque(virus_list)

while q:
    virus, time, x,y = q.popleft()
    if s == time:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and nx < n and ny >=0 and ny < n:
            if data[nx][ny] == 0:
                data[nx][ny] = virus
                q.append((virus, time+1, nx, ny))

print(data[tar_x-1][tar_y-1])