def rotation(arr):
    n = len(arr)
    result = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = arr[i][j]
    return result
            
def check(lock):
    n = len(lock)//3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if(lock[i][j]!=1):
                return False
    return True

def solution(key, lock):
    n = len(key)
    m = len(lock)
    new_lock = [[0]*(m*3) for i in range(m*3)]
    for i in range(m):
        for j in range(m):
            new_lock[i+m][j+m] = lock[i][j]
            
    for i in range(4):
        key = rotation(key)
        for i in range(1,m*2):
            for j in range(1,m*2):
                for x in range(n):
                    for y in range(n):
                        new_lock[i+x][j+y]+=key[x][y]
                
                if check(new_lock):
                    return True
                
                for x in range(n):
                    for y in range(n):
                        new_lock[i+x][j+y]-=key[x][y]
    
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))