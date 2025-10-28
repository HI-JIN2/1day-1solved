from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [False] * (n+1)
    
    def bfs(n, computers, start, visited):
        queue = deque()
        queue.append(start)

        while queue:
            x = queue.popleft()
            visited[x] = True

            for j in range(n):  #012
                if j!=n and computers[x][j] == 1:
                    if visited[j] == False:
                        queue.append(j)

    for com in range(n):
        if visited[com] == False:
            bfs(n,computers, com, visited)
            answer+=1
    return answer