from collections import deque

def solution(people, limit):
    answer = 0
    
    #구명보트 개수 최소화
    # 한 보트당 두명 
    
    people = sorted(people)
    people = deque(people)

    
    while people:
        lastp = people.pop()
        
        if people and lastp + people[0] <= limit: #어차피 두명 밖에 못탐
            people.popleft()
        
        answer+=1
        
            
             
        
    return answer