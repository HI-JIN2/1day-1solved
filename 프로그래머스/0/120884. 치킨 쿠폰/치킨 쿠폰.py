def solution(chicken):
    answer = 0
    other = 0 
    
    l = len(str(chicken))
    
    for i in range(l):
        # print(chicken//10 )
        other += chicken%10 #나머지에 대한 처리가 관건
        chicken = chicken//10 
        answer += chicken
        
    while other:
        other = other//  10
        answer += other
    
    return answer