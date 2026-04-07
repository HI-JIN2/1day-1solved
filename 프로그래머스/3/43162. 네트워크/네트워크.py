def solution(n, computers):
    answer = 0
    
    
    def dfs(i):
        visited[i]= True #방문처리
        for k in range(n): #노드 
            if computers[i][k] == 1 and visited[k] == False: #연결되어 있고 방문 안했어야
                # print(k)
                dfs(k) #방문             
        
        
    visited=[False]*n 
    
    for i in range(n):
        if visited[i] == False:
            # print("시작",i)
            answer+=1 #연결되어 있다면 여기서 다시 시작하지 않음 
            #연결되어 있다면 Dfs에서 돌았었을 것임
            dfs(i)
    
    return answer