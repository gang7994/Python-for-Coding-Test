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
        
g = int(input())
p = int(input())

parent = [0]*(g+1)
for i in range(g+1):
    parent[i] = i

result = 0
for i in range(p):
    plane = find_parent(parent, int(input()))
    if plane == 0:
        break
    result+=1
    union_parent(parent, plane, plane-1)
print(result)