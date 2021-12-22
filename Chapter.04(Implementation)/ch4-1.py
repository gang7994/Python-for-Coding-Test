def access(location,x,y):
    if location[0]+x<1 or location[0]+x>n:
        return False
    if location[1]+y<1 or location[1]+y>n:
        return False
    return True

n = int(input())
move = list(map(str, input().split()))
location = [1,1]

def access(location,x,y):
    if location[0]+x<1 or location[0]+x>n:
        return False
    if location[1]+y<1 or location[1]+y>n:
        return False
    return True

for i in move:
    if i =='L':
        if(access(location, 0,-1)):
            location[1] = location[1]-1;
    elif i == 'R':
        if(access(location, 0,1)):
            location[1] = location[1]+1;
    elif i =='U':
        if(access(location, -1,0)):
            location[0] = location[0]-1;
    else:
        if(access(location, 1,0)):
            location[0] = location[0]+1;

print(location[0],location[1],end='')
            

        
