from collections import deque

def solution(priorities, location):
    answer = 0
    result = []
    q = deque()
    for i, p in enumerate(priorities):
        # print(i,p)
        q.append((i,p))
        
    # print(max(q, key=lambda x: x[1]))
    while q:
        max_p = max(q, key=lambda x: x[1])[1]
        i, p = q.popleft()
        
        if p == max_p:
            #그대로 팝
            result.append(i)
        else:
            q.append((i,p)) #다시 넣어
    # print(result)
    
        
    return result.index(location)+1