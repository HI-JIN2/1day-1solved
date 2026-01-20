def solution(num, total):
    answer = []
    
    
    idx = total//num # 기준점
    
    cnt = num//2
    
    for i in range(idx-cnt,idx+cnt+1):
        answer.append(i)
        
        
    if sum(answer) == total:
        return answer
    else:
        return answer[1:]
    
    return answer