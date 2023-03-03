N, M = map(int, input().split())
chessboard = []
count = []

for _ in range(N):
    chessboard.append(input())

for a in range(N-7):
    for b in range(M-7):#8개보다 클 때, 큰 숫자마다 하나씩 더 돌려줌
        Start_W = 0
        Start_B = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: #인덱스의 합이 짝수
                    if chessboard[i][j] != 'W': #W로 색칠되어야 함
                        Start_W += 1
                    if chessboard[i][j] != 'B': #B로 색칠되어야 함
                        Start_B += 1
                else: #인덱스의 합이 홀수
                    if chessboard[i][j] != 'B':
                        Start_W += 1
                    if chessboard[i][j] != 'W':
                        Start_B += 1
        count.append(min(Start_W, Start_B))

print(min(count))