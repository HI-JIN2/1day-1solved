from collections import deque

def solution(numbers, target):
    
    
    
    def bfs(index,total): #큐에 먼저 넣고 방문처리
        answer = 0
        q = deque()
        q.append((index,total))
        
        while q:
            i, t = q.popleft()
            if i == len(numbers):
                if t ==target:
                    answer+=1
            else:
                q.append((i+1, t+numbers[i]))
                q.append((i+1, t-numbers[i]))
        return answer
        
            
    return bfs(0,0)