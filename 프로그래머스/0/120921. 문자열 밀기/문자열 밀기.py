def solution(A, B):
    answer = 0
    
    if A == B:
        return 0
    
    idx = 0
    
    max_idx = len(A) #5
    
    while True:
        result = ""
        result+=A[-1]
        result+=A[:-1]
        idx+=1
        # print(idx, result)

        if result == B:
            return idx
        
        elif idx > max_idx:
            # print(idx)
            return -1
        
        A = result
        
    return answer