def solution(s):
    list_s = list(s)
    
    stack =[]
    
    for i in list_s:
        if stack:
            if i == "(":
                stack.append(i)
            else: 
                stack.pop()            
        else:
            stack.append(i)

    if stack:
        return False
    else:
        return True