from collections import deque

n,m, k = map(int,input().split())

graph = [[0 for _ in range(m+1)] for _ in range(n+1)]
#0행 0열은 버리기
# print(graph)

for i in range(k):
    r,c = map(int,input().split()) #r이 세로
    graph[r][c] = 1

#가장 큰 사이즈 구하기
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(y,x):
    queue = deque()
    queue.append((y,x))

    temp = 0

    while queue:
        y,x = queue.popleft()

        if graph[y][x] ==1:
            # print("--",x,y)
            temp+=1
            graph[y][x] = 0  # 방문처리

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<1 or nx>m or ny<1 or ny>n:
                continue

            if graph[ny][nx] == 1: #가보지 않았고 쓰레기임
                # print(nx,ny)
                queue.append((ny,nx))
                graph[ny][nx] = 0 #미리 방문처리
                temp+=1
    # print(temp)
    return temp

answer = [0 ]
for i in range(1,n+1): #세로
    for j in range(1,m+1): #가로
        if graph[i][j] == 1: #방문하지 않았고, 쓰레기면
            # print(i,j)
            trash_size = bfs(i,j)
            answer.append(trash_size)
            # print(trash_size)

answer.sort(reverse=True)

print(answer[0])