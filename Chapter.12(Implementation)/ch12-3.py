def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        temp = s[0:i]
        count = 1
        string = ""
        for j in range(i,len(s),i):
            if temp == s[j:j+i]:
                count+=1
            else:
                string += str(count) + temp if count>=2 else temp
                temp = s[j:j+i]
                count = 1
        string += str(count) + temp if count>=2 else temp
        answer = min(answer,len(string))
    return answer

s = "aabbaccc"
print(solution(s))