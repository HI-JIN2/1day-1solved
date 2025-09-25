import math

def solution(progresses, speeds):
    answer = []
    
    remain = [ math.ceil((100-progresses[i]) / speeds[i])  for i in range(len(progresses))]
    print(remain)
    
    
    nowdays = remain[0]
    cnt = 1
    
    # print(remain[1:])
    for i in remain[1:]:
        # print(i,"입니다")
        if i<=nowdays:
            cnt +=1
            # print(i,cnt)
        else: # i >nowdays
            answer.append(cnt)
            nowdays = i
            cnt =1
            # print(i,cnt)
    answer.append(cnt)
    # print(answer)
    
    return answer