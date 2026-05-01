def solution(dots):
    
    #무조건 4개
    #경우의수가 13 24 / 12 34 / 14 23
    if abs(dots[0][0]-dots[1][0]) / abs(dots[0][1]-dots[1][1]) == abs(dots[2][0]-dots[3][0]) / abs(dots[2][1]-dots[3][1]):
        return 1
    elif abs(dots[0][0]-dots[2][0]) / abs(dots[0][1]-dots[2][1]) == abs(dots[1][0]-dots[3][0]) / abs(dots[1][1]-dots[3][1]):
        return 1
    elif abs(dots[0][0]-dots[3][0]) / abs(dots[0][1]-dots[3][1]) == abs(dots[1][0]-dots[2][0]) / abs(dots[1][1]-dots[2][1]):
        return 1
    else: return 0