from bisect import bisect_left,bisect_right

def FindCount(arr, lvalue, rvalue):
    left = bisect_left(arr, lvalue)
    right = bisect_right(arr, rvalue)
    return right - left



def solution(words, queries):
    answer = []
    arr = [[] for i in range(10001)]
    reverse_arr = [[] for i in range(10001)]
    for i in words:
        arr[len(i)].append(i)
        reverse_arr[len(i)].append(i[::-1])
    for i in range(10001):
        arr[i].sort()
        reverse_arr[i].sort()
    
    for q in queries:
        if q[0] != "?":
            count = FindCount(arr[len(q)], q.replace('?','a'), q.replace('?','z'))
        else:
            count = FindCount(reverse_arr[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z'))
        answer.append(count)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))