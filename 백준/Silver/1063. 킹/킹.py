king, stone, n  = input().split()
n = int(n)

data = []
for i in range(n):
    d = input()
    data.append(d)
# print(data)

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,1,-1,-1]
direction = ['R', 'L', 'B', 'T', 'RT', 'LT','RB','LB']


king_x = int(ord(king[0])-ord('A')+1)
king_y = int(king[1])

stone_x = int(ord(stone[0])-ord('A')+1)
stone_y = int(stone[1])

is_fail = 0

for i in data:
    # print(i)
    for t in range(len(direction)):
        if i == direction[t]:
            nx = king_x + dx[t] #초기화 안해도 파이썬은 가능
            ny = king_y + dy[t]

            if nx == stone_x and ny == stone_y: #돌이랑 겹치면
                newstonex = stone_x + dx[t]
                newstoney = stone_y + dy[t]
                # print("돌이랑 겹쳐요", nx,ny, newstonex,newstoney)

                if newstonex < 1 or newstoney <1 or newstonex >8 or newstoney >8 :
                    # print("돌을 밀면 떨어져요")
                    is_fail = 1
                    continue

                stone_x = newstonex
                stone_y = newstoney

    if is_fail ==1:
        is_fail =0
        continue

    if nx<1 or ny < 1 or nx >8 or ny> 8:
        continue

    king_x = nx
    king_y = ny


# 결과
king = chr(king_x+65-1)+ str(king_y)
stone = chr(stone_x+65-1)  + str(stone_y)

print(king)
print(stone)