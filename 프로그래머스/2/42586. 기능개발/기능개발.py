from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    q=deque()
    for i in range(len(progresses)):
        q.append((progresses[i], speeds[i]))
    # print(q)
    
    now = math.ceil((100-progresses[0])/speeds[0])
    
    result = 0
    for p,s in q:
        day = math.ceil((100-p)/s)
        # print(p,s,day)
        if now>=day: #7 > 7 , 7 >3 
            result +=1
            
        else: #now<day 9>3
            answer.append(result)
            now = day
            result = 1
            #이 조건에 더해야할때 
    answer.append(result)
        
    return answer