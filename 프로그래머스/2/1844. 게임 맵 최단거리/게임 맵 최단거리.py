from collections import deque

def solution(maps):
    answer = 0
    n = len(maps) #세로
    m = len(maps[0]) #가로
    
    def bfs(r,c):
        q = deque()
        q.append((r,c))
        dist[r][c]=1
        
        while q:
            r,c = q.popleft()
            
            for dr, dc in ((0,1), (0,-1),(1,0),(-1,0)):
                nr = dr+r
                nc = dc+c
                
                if 0>nr or nr>=n or 0>nc or nc>=m: #범위 제한
                    continue
                
                elif maps[nr][nc] == 1 and dist[nr][nc] ==-1: # 갈 수 있어야하며 안갔어야함
                    dist[nr][nc] = dist[r][c]+maps[nr][nc] #이전까지의 거리+1
                    q.append((nr,nc))
                    
    dist = [ [-1]* m for _ in range(n)]
    # print(dist)
    bfs(0,0)
    # print(dist)
    return dist[n-1][m-1]
