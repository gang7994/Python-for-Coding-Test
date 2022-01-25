def find_parent(parent, x):
    if parent[x] !=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n,m = map(int, input().split())
parent = [0]*(n)
for i in range(n):
    parent[i] = i
graph = []
for i in range(m):
    a,b,cost = map(int, input().split())
    graph.append((cost, a, b))
    
graph.sort()
on = 0
total = 0
for i in graph:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        on+=cost
    total+=cost
print(total-on)
    
