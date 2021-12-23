loc = input()

x = ord(loc[0])-97
y = int(loc[1])-1
count = 0
arr = [[x-2,y-1],[x-1,y-2],[x+1,y-2],[x+2,y-1],[x-2,y+1],[x-1,y+2],[x+1,y+2],[x+2,y+1]]

for i in arr:
    if i[0]>=0 and i[0]<=7 and i[1]>=0 and i[1]<=7:
        count+=1
        
print(count)