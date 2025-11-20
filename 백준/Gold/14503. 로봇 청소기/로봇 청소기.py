# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 2. 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 없는 경우,
#   1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
#   2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 3. 현재 칸의 주변 $4$칸 중 청소되지 않은 빈 칸이 있는 경우,
#   1. 반시계 방향으로 $90^\circ$ 회전한다.
#   2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
#   3. 1번으로 돌아간다.


n,m = map(int,input().split())

y,x,d= map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

#print(graph)

answer = 0

# 북, 동, 남, 서
dy = [-1, 0, 1, 0]   # y는 행 방향 (위아래)
dx = [0, 1, 0, -1]   # x는 열 방향 (좌우)

#시작위치
if graph[y][x] == 0:
    answer +=1 #청소함
    graph[y][x] = 2

while True:
    temp = 0 #청소 했는지 안했는지 플래그

    for _ in range(4):
        nx = x + dx[(d + 3) % 4]
        ny = y + dy[(d + 3) % 4] #이게 중요
        d = (d + 3) % 4

        if nx<0 or nx>=m or ny<0 or ny>=n:
            # print(answer)
            # exit() #벽에 부딪히면 종료
            continue

        if graph[ny][nx] == 0:
            y,x = ny,nx #전진
            graph[ny][nx] = 2 #청소
            answer +=1
            temp = 1
            break #다른 방향은 안봄

    if temp == 0: #청소 하나도 못했음 후진
        by = y-dy[d]
        bx = x-dx[d]

        if graph[by][bx] == 1: #벽이라 후진 못하면
            print(answer)
            exit()
        y,x = by,bx
        temp=1

