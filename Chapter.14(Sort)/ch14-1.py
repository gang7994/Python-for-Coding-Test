n = int(input())
student = []
for i in range(n):
    name, kor, eng, math = map(str, input().split())
    student.append([int(kor), int(eng), int(math), name])
    
student.sort(key = lambda x:(-x[0],x[1],-x[2],x[3]))

for i in range(n):
    print(student[i][3])