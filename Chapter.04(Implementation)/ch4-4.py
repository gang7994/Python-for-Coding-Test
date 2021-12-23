n,m = map(int, input().split())
x,y,dir = list(map(int, input().split()))
mmp = []
for i in range(n):
    mmp.append(list(map(int, input().split())))
d = [[0]*m for _ in range(n)]
def turn():
    global dir
    dir-=1
    if dir ==-1:
        dir = 3
    
dx = [-1,0,1,0] #n
dy = [0,1,0,-1] #m

d[x][y] = 1
count = 1
turncount = 0
while True:
    turn()
    new_x = x + dx[dir]
    new_y = y + dy[dir]
    if d[new_x][new_y] == 0 and mmp[new_x][new_y] == 0:
        x = new_x
        y = new_y
        count+=1
        d[x][y] = 1
        turncount = 0
    else:
        turncount+=1
    
    if turncount == 4:
        new_x = x - dx[dir]
        new_y = y - dy[dir]
        if(mmp[new_x][new_y] == 0):
            x = new_x
            y = new_y
        else:
            break
        turncount = 0
        
print(count)