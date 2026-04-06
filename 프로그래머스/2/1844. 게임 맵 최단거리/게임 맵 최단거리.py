from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dist = [ [-1]*m for _ in range(n)]

    def bfs(r,c):
        #출발지인 0,0에서 부터 닿을 수 있는 모든 지점까지의 거리를 구할 것임
        q = deque()
        q.append((r,c))
        dist[r][c] = 0 #출발지에서 출발지까지의 거리는 0 

        while q:
            r,c = q.popleft()

            for dr,dc in ((1,0), (-1,0), (0,1),(0,-1)):
                nr = dr+r
                nc = dc+c

                if 0>nr or nr>=n or 0>nc or nc>=m:
                    continue #범위 아웃

                elif dist[nr][nc] == -1 and maps[nr][nc] == 1: #안가야하고 갈 수 있는 곳만
                    q.append((nr,nc))
                    dist[nr][nc] = dist[r][c] +1 #bfs는 큐에 넣고 선 처리
                    # print(nr,nc,dist[nr][nc])

    bfs(0,0) #출발지가 하나이기 때문에 bfs를 한번만 호출
  
    # print(dist)

    
    if dist[n-1][m-1] == -1:
        return -1
    else: 
        return dist[n-1][m-1]+1