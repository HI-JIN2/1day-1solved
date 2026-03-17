import math
def solution(citations):
    answer = 0
    citations.sort(reverse=True)    
    for index, c in enumerate(citations):
        # print(index+1,c)
        if c>=index+1:
            answer = index+1
    return answer