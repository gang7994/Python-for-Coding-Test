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
    
n, m = map(int, input().split())

parent = [0] *(n+1)
for i in range(n+1):
    parent[i] = i
    
for i in range(m):
    calculate, a, b = map(int, input().split())
    if calculate == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")