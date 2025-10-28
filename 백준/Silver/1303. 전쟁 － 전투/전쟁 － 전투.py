from collections import deque

n,m = map(int,input().split())
graph = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(m):
    graph.append(list(input().strip()))
# print(graph)

visited = [[False for i in range(n)] for j in range(m)]
# print(visited)

def bfs(x,y,target):
    queue = deque()
    queue.append((y,x))
    # visited[y][x] = True
    temp = 0

    if graph[y][x] == target:
        temp+=1
        graph[y][x]='A'

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            if graph[ny][nx] == 'A': #바꾼거 걸러
                continue
            # print("next",nx,ny)

            if graph[ny][nx] ==target:
                # print(nx,ny)
                temp+=1
                graph[ny][nx] = 'A' #중복처리
                queue.append((ny,nx))
    # print(temp)
    return temp



my = 0
for i in range(n):
    for j in range(m):
        if graph[j][i] == 'W':
            knight = bfs(i,j,'W')
            my += knight*knight
print(my)

# print(graph)
others = 0
for i in range(n):
    for j in range(m):
        if graph[j][i] == 'B':
            knight = bfs(i,j,'B')
            others += knight*knight
print(others)
# print(graph)