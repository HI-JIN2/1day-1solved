import math

n = int(input())


like = {}

seat = [[0] * n for i in range(n)]
# print(seat)

order = [] #순서

for i in range(n*n):
    a,b,c,d,e = map(int,input().split())
    order.append(a)
    like[a] = {b,c,d,e}

#자리 배치
# 맨처음 학생 가운데

dr = [-1,1,0,0]
dc = [0,0,-1,1]


# 우선 순위 => 좋아하는 학생 많음, 빈칸이 가장 많은, 행 작음, 열 작음


def set_seat(student):
    best = (-1,-1,0,0)
    best_seat = (0,0)

    for r in range(n):
        for c in range(n):
            if seat[r][c] !=0:
                continue

            like_cnt = 0
            empty_cnt =0

            for d in range(4):
                nr = r+ dr[d]
                nc = c +dc[d]

                if 0 <= nr <n and 0 <= nc<n :
                    if seat[nr][nc] in like[student]:
                        like_cnt+=1 #좋아하는 학생
                    elif seat[nr][nc] == 0 :
                        empty_cnt  += 1 #빈자리

            priority = (like_cnt, empty_cnt, -r, -c)
            if priority>best:
                best = priority
                best_seat = (r,c)


    r,c = best_seat
    seat[r][c] = student


for i in order:
    set_seat(i)



# print(seat)


#자리 반환이 아니라 만족도를 반환

score = [0,1,10,100,1000]


result =0

for r in range(n):
    for c in range(n):

        student = seat[r][c]
        cnt =0

        for d in range(4):
            nr = r+dr[d]
            nc = c+dc[d]

            if 0<= nr <n and 0<=nc<n:
                if seat[nr][nc] in like[student]:
                    cnt +=1

        result += score[cnt]
print(result)