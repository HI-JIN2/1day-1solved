from collections import deque
m,n = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = []

queue = deque()

def bfs():
    while queue:
        y,x = queue.popleft()
        # print(y,x)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue

            if graph[ny][nx] == -1:
                continue

            if graph[ny][nx] == 0 :
                graph[ny][nx]= graph[y][x] + 1
                queue.append((ny,nx))
        # print(days)
        # print(graph)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: #1이면 bfs 실시
            queue.append((i,j))

bfs()

days = 0

for row in graph:
    if 0 in row:
        print(-1)
        exit()
    days=max(days,max(row))

print(days-1)