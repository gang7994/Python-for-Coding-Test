arr = input()
front = 0
back = 0
n = len(arr)//2
for i in arr[:n]:
    front+=int(i)
for i in arr[n:]:
    back+=int(i)    
    
if front==back:
    print('LUCKY')
else:
    print('READY')