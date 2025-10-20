n = int(input())

# 동북서남
# 시뮬레이션 완전탐색
dx = [0,0,-1,1]
dy = [ -1,1,0,0 ]
move_type = ["L","R","U","D"]

# R 동
# U 북
# D 남
# L 서

# 출발지 1,1
x,y =1,1
data = list(input().split())

for i in data:
    for t in range(len(move_type)):
        if i == move_type[t]:
            nx = x + dx[t]
            ny = y + dy[t]

    if nx <1 or ny < 1 or nx >n or ny>n:
        continue

    x = nx
    y = ny


print(x,y)