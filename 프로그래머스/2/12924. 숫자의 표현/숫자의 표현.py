def solution(n):
    answer = 0
    
    for i in range(n,0,-1):
        s = 0
        for j in range(i,0,-1):
            s+=j
            if s==n:
                answer+=1
                break
                # print(i,j)
            if s > n:
                break
        
    return answer