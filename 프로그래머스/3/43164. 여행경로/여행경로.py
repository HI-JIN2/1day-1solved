def solution(tickets):
    answer = []
    
    def dfs(start):
        if len(tickets) == 0:
            return True
        
        alist = list(filter(lambda x: x[0] == start, tickets)) #start로 시작하는 후보군 리스트
        alist.sort(key = lambda x: x[1]) #도착지 이름으로 오름차순 정렬
        
        for a in alist:
            answer.append(a[1])
            tickets.remove(a)
            
            if dfs(a[1]): #true 반환하면 
                return True
            
            answer.pop() #false 반환하면
            tickets.append(a)
        
        return False
  
    answer.append("ICN")
    dfs("ICN")    
    
    return answer