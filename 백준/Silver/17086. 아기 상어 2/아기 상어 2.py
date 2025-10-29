from collections import deque

n, m = map(int,input().split()) #세로,가로
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))
# print(graph)

visited = [[ False for i in range(m)] for i in range(n)]
# print(visited)

dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]
queue = deque()

def bfs():
    # queue.append((y,x))
    # visited[y][x] = True

    cnt = 0

    while queue:
        y,x = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=m or ny<0 or ny >=n:
                continue

            if graph[ny][nx] == 1:
                continue

            if graph[ny][nx] == 0: #0이면
                graph[ny][nx] = graph[y][x]+1
                queue.append((ny,nx))
    return cnt

answer = []
for y in range(n):
    for x in range(m):
        if graph[y][x]==1: #상어가 1
            queue.append((y,x))

bfs()

for a in graph:
    answer.append(max(a))

print(max(answer)-1)
