# 8x8


def solution(data):
    answer =0

    # dx = [ 0,0,-1,1]
    # dy = [1,-1,0,0]

    dx = [ 1,1,-1,-1,-2,-2,2,2]
    dy = [2,-2,-2,2,1,-1,1,-1]

    x= ord(data[0])-ord('a')+1
    y= int(data[1])

    # print(len(dx))
    # print(x,y)

    for i in range(len(dx)):
        nx = x+dx[i]
        ny = y+dy[i]
        # print(i,"==",nx,ny)
        if nx <1 or ny <1 or nx>9 or ny>9:
            # print("실패")
            continue
        # print("성공")
        answer +=1

    return answer



print(solution('a1'))
print(solution('c2'))