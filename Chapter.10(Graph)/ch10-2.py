def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    


v, e = map(int, input().split())
edge = []
parent = [0] *(v+1)
for i in range(v+1):
    parent[i] = i

for i in range(e):
    a, b, cost = map(int, input().split())
    edge.append((a,b,cost))
    
edge.sort(key = lambda x:x[2])


result = 0
last = 0

for i in edge:
    a, b, cost = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result-last)