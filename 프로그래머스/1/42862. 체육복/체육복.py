def solution(n, lost, reserve):
    answer = 0
    
    common = set(lost) & set(reserve) #교집합 - 여벌도 있었는데 도난도 당했으면 본인거임. 
    lost = list(set(lost) - common)
    reserve = list(set(reserve) - common)
    
    answer = n - len(lost)
    
    reserve.sort()
    lost.sort()
    
    for i in lost:
        for j in reserve:
            if abs(i-j) <= 1:
                answer += 1
                reserve.remove(j) #한번 빌려준 사람은 또 못빌려줌 
                break  #i는 빌릴 사람 찾았으니 break
    
    return answer