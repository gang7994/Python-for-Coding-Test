from collections import deque

t = int(input())
for case in range(t):
    n = int(input())
    degree = [0] * (n+1)
    graph =[[False] * (n+1) for _ in range(n+1)]
    team = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1,n):
            graph[team[i]][team[j]] = True
            degree[team[j]] += 1
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            degree[b]-=1
            degree[a]+=1
        else:
            graph[a][b] = True
            graph[b][a] = False
            degree[a]-=1
            degree[b]+=1
    result = []
    q = deque()
    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)
    state = 0 #정상 0, 사이클 1, 중복 2
    for i in range(n):
        if len(q)>=2:
            state = 2
            break
        if len(q)==0:
            state = 1
            break
        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                degree[j]-=1
                if degree[j] == 0:
                    q.append(j)
    if state == 1:
        print("IMPOSSIBLE")
    elif state == 2:
        print("?")
    else:
        for ii in result:
            print(ii, end=' ')
        print()