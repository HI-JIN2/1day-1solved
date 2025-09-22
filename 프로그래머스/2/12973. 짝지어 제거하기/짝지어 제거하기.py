def solution(s):
    if len(s) == 0 :
        return 0
    
    answer = -1

    list_s = list(s)
    stack = []
    
    for i in list_s:
        if stack:
            if stack[-1] == i:
                stack.pop()
            elif stack[-1] != i:
                stack.append(i)
        else: 
            stack.append(i)            
    
    if stack:
        return 0
    else: 
        return 1
    

    return answer