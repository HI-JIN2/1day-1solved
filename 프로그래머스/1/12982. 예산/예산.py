def solution(d, budget):
    answer = 0
    
    #최대 몇개 부서까지 지원을 해주려면 그리디로 적은 예산을 필요로 하는 부서부터 준다
    d.sort()
    
    for i in d:
        if i<=budget:
            answer+=1
            budget-=i
    
    return answer