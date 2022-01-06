arr = list(map(int, input()))

group_0 = 0 
group_1 = 0
if arr[0]==0:
    group_0+=1
else:
    group_1+=1
    
for i in range(1,len(arr)):
    if arr[i] == 0:
        state = 0
    else: 
        state = 1
    if arr[i] != arr[i-1]:
        if state == 0:
            group_0+=1
        else:
            group_1+=1

if group_1 > group_0:
    print(group_0)
else:
    print(group_1)
 