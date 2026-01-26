def solution(array):
    answer = 0
    
    for n in array:
        for i in str(n):
            if '7' in i:
                answer+=1
    
    return answer