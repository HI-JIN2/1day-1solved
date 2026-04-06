import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int,input().split())

data = [ list(map(int,input().split())) for _ in range(n)]
# print(data)
dist = [[-1]*m for _ in range(n)] #기본 값 -1

def bfs(r,c):
    q= deque()
    q.append((r,c))
    dist[r][c] = 0 #애초에 목표지점인 2에서 호출을 하니까

    while q:
        r,c = q.popleft()

        for dr, dc in ( [0,1], [1,0], [0,-1], [-1,0]):
            nr= r+dr
            nc = c+dc

            if 0>nr or nr>=n or 0>nc or nc>=m:
                continue
            elif data[nr][nc] == 1 and dist[nr][nc]==-1: #그 범위여야만 & 갈 수 있어야만 & 방문을 안했어야만
                q.append((nr,nc))
                dist[nr][nc] = dist[r][c]+1 # 선방문 처리
            else:
                continue



# print(dist)

for r in range(n):
    for c in range(m):
        if data[r][c] == 2:
            bfs(r,c)
            dist[r][c] = 0
        elif data[r][c] == 0: #원래 갈 수 없으면 0
            dist[r][c] = 0

for r in range(n):
    print(*dist[r])