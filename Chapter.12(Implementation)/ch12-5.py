n = int(input())
k = int(input())
data = [[0]*n for i in range(n)]
for i in range(k):
    x,y = map(int, input().split())
    data[x-1][y-1] = 1

l = int(input())
info = [] 
for i in range(l):
    x,c = input().split()
    info.append((int(x),c))   
    
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(dir, c):
    if c =='D':
        dir = (dir+1)%4
    else:
        dir = (dir-1)%4
    return dir

def game():
    x,y = 0, 0
    data[x][y] = 1
    dir = 0 #동남서북
    time = 0
    rotate = 0 #명령어 실행횟수
    q = [(x,y)]
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx>=0 and nx<n and ny>=0 and ny<n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx,ny))
                px,py = q.pop(0)
                data[px][py] = 0
            else:
                data[nx][ny] = 2
                q.append((nx,ny))
        else:
            time += 1
            break
        time += 1
        x, y = nx, ny
        if rotate < l and time == info[rotate][0]:
            dir = turn(dir,info[rotate][1])
            rotate+=1
    return time

print(game())