def solution(i, j, k):
    answer = 0
    
    for num in range(i,j+1):
        for n in map(int,list(str(num))):
            if n ==k:
                answer += 1

    return answer