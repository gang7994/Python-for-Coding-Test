def solution(N, stages):
    answer = []
    length = len(stages)
    for i in range(1,N+1):
        son = stages.count(i)
        if length == 0:
            fail = 0
        else:
            fail = son / length
        length-=son
        answer.append([i,fail])
    answer.sort(key = lambda x:-x[1])
    result = []
    for i in answer:
        result.append(i[0])
    return result


