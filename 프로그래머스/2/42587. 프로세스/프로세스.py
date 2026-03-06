from collections import deque
def solution(priorities, location):
    answer = []
    
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((i,p))
    # print(queue)
    
    while queue:
        i,p = queue.popleft()
        if len(queue) ==0 :
            answer.append(i) #마지막 원소
            break
        if p < max(q[1] for q in queue):
            # print(i,p)
            queue.append((i,p))
        else: #max라면
            answer.append(i)
        
    # print(answer)
    
    return answer.index(location)+1