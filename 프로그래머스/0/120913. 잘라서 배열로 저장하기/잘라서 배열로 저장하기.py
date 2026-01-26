def solution(my_str, n):
    answer = []
    
    for i in range(len(my_str)//n+1):
        ans = my_str[i*n:i*n+n]
        if ans:  
            answer.append(ans)
        
        
    return answer