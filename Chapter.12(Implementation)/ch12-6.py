def add_check(blueprint, a, b, c):
    if c == 0: #기둥
        if b == 0: #바닥인경우
            return True
        elif [a,b-1,0] in blueprint: #밑이 기둥인경우
            return True
        elif ([a-1,b,1] in blueprint) or ([a,b,1] in blueprint): #보한쪽 끝에 있는경우
            return True
        return False
    else: #보
        if([a,b-1,0] in blueprint) or ([a+1,b-1,0] in blueprint): #기둥위에 있는 경우
            return True
        elif ([a-1,b,1] in blueprint) and ([a+1,b,1] in blueprint):
            return True
        return False
    
def del_check(blueprint, a, b, c):
    if c == 0: #기둥
        if ([a,b+1,0] in blueprint):
            return False
        if ([a-1,b+1,1] in blueprint) and (([a,b+1,1] not in blueprint) or ([a-2,b+1,1] not in blueprint)) and ([a-1,b,0] not in blueprint):
            return False
        if ([a,b+1,1] in blueprint) and (([a-1,b+1,1] not in blueprint) or ([a+1,b+1,1] not in blueprint)) and ([a+1,b,0] not in blueprint):
            return False
        return True    
    else: #보
        if ([a,b,0] in blueprint) and (([a,b-1,0] not in blueprint) and ([a-1,b,1] not in blueprint)):
            return False
        if ([a+1,b,0] in blueprint) and (([a+1,b-1,0] not in blueprint) and ([a+1,b,1] not in blueprint)):
            return False
        if ([a-1,b,1] in blueprint) and (([a-1,b-1,0] not in blueprint) and ([a,b-1,0] not in blueprint)):
            return False
        if ([a+1,b,1] in blueprint) and (([a+1,b-1,0] not in blueprint) and ([a+2,b-1,0] not in blueprint)):
            return False
        return True
        
    
def solution(n, build_frame):
    blueprint = []
    for i in build_frame:

        if i[3] == 1:
            if add_check(blueprint, i[0], i[1], i[2]):
                blueprint.append([i[0],i[1],i[2]])
                
        else:
            if del_check(blueprint, i[0], i[1], i[2]):
                blueprint.remove([i[0], i[1], i[2]])
    blueprint.sort()            
    return blueprint



build_frame =[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
n = 5

print(solution(n,build_frame))

#########################################################
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝 부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False # 아니라면 거짓(False) 반환
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False # 아니라면 거짓(False) 반환
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치
        if operate == 1: # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer) # 정렬된 결과를 반환