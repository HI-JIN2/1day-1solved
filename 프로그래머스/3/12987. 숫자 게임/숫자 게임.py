def solution(A, B):
    answer = 0
    
    
    A.sort(reverse = True)
    B.sort(reverse = True)
    indexA=0
    indexB=0
    
    for i in range(len(A)):
        if A[indexA]<B[indexB]:
            indexA+=1
            indexB+=1
            answer+=1
        else: 
            B.pop()
            indexA+=1
            
    return answer