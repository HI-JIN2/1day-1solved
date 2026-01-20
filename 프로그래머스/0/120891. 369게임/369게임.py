def solution(order):
    answer = 0
        
    for i in map(int,str(order)):
        if i in [3,6,9]:
            answer+=1
    return answer