# 종료가 안되는 법칙???
import sys

input = sys.stdin.readline


n,k = map(int,input().split()) #체스판의 크기, 말의 개수
pan = [ list(map(int,input().split())) for _ in range(n)]
# 0 흰 , 1 빨, 2파

horse = [ list(map(int,input().split())) for _ in range(k)]
#행, 열, 이동방향
for h in horse:
    h[0], h[1] = (h[1] - 1, h[0] - 1) #좌표 보기 쉽게 한번에 바꿈

#보드에 있는 말 근황. 한 칸에 말 여러개 있는거 관리
board = [ [ [] for _ in range(n)] for _ in range(n)] #앞에 있는 말이 젤 아래

for i,h in enumerate(horse):
    x,y,d = h
    board[x][y].append(i+1)


# x,y
d = [
    [0,0],
    [1,0], # ->
    [-1,0], #<-
    [0,-1], #위로
    [0,1] #아래로
]



def move_white(nx,ny, moving):
    board[nx][ny].extend(moving)
    for num in moving:
        horse[num-1][0] = nx
        horse[num-1][1] = ny

def move_red(nx, ny, moving ):
    moving = moving[::-1]#반대로
    board[nx][ny].extend(moving)
    for num in moving:
        horse[num-1][0] = nx
        horse[num-1][1] = ny



def blue_or_out(nx, ny):
    return not (0 <= nx < n and 0 <= ny < n) or pan[ny][nx] == 2

for turn in range(1,1001): #반복문을 뭘로 해야할지
    for i,h in enumerate(horse):

        x,y = h[0],h[1] #말 현재 위치
        if board[x][y][0]!= i+1: #1번말부터 도는데 본인 차례에 맨밑이 아니면 움직일 수 없음
            continue

        #다음칸 정의
        #칸 안넘치는지 점검
        if h[2] == 1:
            nx,ny  = h[0]+1 , h[1]
        elif h[2] == 2:
            nx,ny = h[0]-1, h[1]
        elif h[2] == 3:
            nx,ny = h[0], h[1]-1
        elif h[2] == 4:
            nx,ny = h[0], h[1]+1

        if blue_or_out(nx, ny):
            if horse[i][2] == 1:
                horse[i][2] = 2
            elif horse[i][2] == 2:
                horse[i][2] = 1
            elif horse[i][2] == 3:
                horse[i][2] = 4
            elif horse[i][2] == 4:
                horse[i][2] = 3

            # 반대 방향으로 다시 계산
            nd = horse[i][2]
            nx = x + d[nd][0]
            ny = y + d[nd][1]

            # 또 파란색 or 범위밖이면 이동 안 함
            if blue_or_out(nx, ny):
                continue


        if pan[ny][nx] == 0: #만약에 이동한 칸이 흰
            moving = board[x][y][:]
            move_white(nx,ny, moving) #현재칸의 말을 함께 넘김
            board[x][y].clear()


        elif pan[ny][nx] == 1:
            moving = board[x][y][:]

            move_red(nx,ny,moving)
            board[x][y].clear()

        if len(board[nx][ny]) >= 4:
            print(turn)
            sys.exit()

print(-1)
