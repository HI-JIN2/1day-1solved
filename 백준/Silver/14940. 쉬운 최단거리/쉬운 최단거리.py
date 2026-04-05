from collections import deque

n, m =map(int,input().split())

data = [  list(map(int,input().split()))  for _ in range(n)]

# print(data)

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r,c):
    q = deque()
    q.append((r,c))

    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = dr[i]+r
            nc = dc[i]+c

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if data[nr][nc] == 0:
                continue
            if data[nr][nc] == 1 and dist[nr][nc] == -1: #갈 수 있고, 방문 안한곳만
                q.append((nr,nc))
                dist[nr][nc] = dist[r][c]+1

dist = [ [ -1 ]*m for _ in range(n)]
# visited = [[False]*m for _ in range(n)]

for r in range(n):
    for c in range(m):
        if data[r][c] == 2:# 목표 지점
            dist[r][c] = 0
            bfs(r,c)
        elif data[r][c] == 0: #원래 0이면 0임
            dist[r][c] = 0

for r in range(n):
    print(*dist[r] ,end="\n")
