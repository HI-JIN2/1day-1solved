from collections import deque

n=int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().strip())))
# print(graph)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    home = 0
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx >=n or ny<0 or ny >=n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                home +=1
                queue.append((nx,ny))
    if home == 0:
        return 1
    return home

danji = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home = bfs(i,j)
            danji.append(home)



print(len(danji))
danji.sort()
for i in danji:
    print(i)

