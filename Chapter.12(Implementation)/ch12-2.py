arr = input()
ar  =sorted(arr)
result = 0
for i in ar:
    tmp = ord(i)
    if(tmp <= 57 and tmp >= 48):
        result+=(tmp-48)
    else:
        print(i,end='')

if result !=0:
    print(result)