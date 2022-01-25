def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
n = int(input())
x = []
y = []
z = []
edge = []
for i in range(1,n+1):
    arr = list(map(int, input().split()))
    x.append((arr[0],i))
    y.append((arr[1],i))
    z.append((arr[2],i))
    
x.sort()
y.sort()
z.sort()
result = 0
parent = [0] *(n+1)
for i in range(1,n+1):
    parent[i] = i
for i in range(n-1):
    edge.append((abs(x[i][0]-x[i+1][0]), x[i][1], x[i+1][1]))
    edge.append((abs(y[i][0]-y[i+1][0]), y[i][1], y[i+1][1]))
    edge.append((abs(z[i][0]-z[i+1][0]), z[i][1], z[i+1][1]))
edge.sort()
for i in edge:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)