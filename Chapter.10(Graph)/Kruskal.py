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

v, e = map(int, input().split())
parent = [0] * (v+1)
edges = []
result = 0

for i in range(1,v+1):
    parent[i] = i
    
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))
    
edges.sort(key=lambda x:x[2])

for i in edges:
    a, b, cost = i
    if find_parent(parent, a) != find_parent(parent, b):
        result+=cost
        union_parent(parent, a, b)
        
print(result)
print(parent)