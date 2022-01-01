INF = int(1e9)

n, m = map(int, input().split()) # n : 노드개수, m : 간선의 개수 

graph = [[INF] * (n+1) for i in range(n+1)]

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i == j):
            graph[i][j] = 0
            
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] != INF:
            print(graph[i][j],end=' ')
        else:
            print('?',end=' ')
    print()
    
'''입력값
4 7 
1 2 4
1 4 6
2 1 3
2 3 7 
3 1 5
3 4 4
4 3 2
'''
'''출력값
0 4 8 6 
3 0 7 9
5 9 0 4
7 11 2 0
'''