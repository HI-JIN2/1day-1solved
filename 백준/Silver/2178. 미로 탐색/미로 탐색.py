from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m=map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx>=m or ny<0 or ny>=n:
                continue

            if graph[ny][nx] ==0:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] =  graph[y][x]+1
                queue.append((nx,ny))


bfs(0,0)
print(graph[n-1][m-1])
# print(graph)
