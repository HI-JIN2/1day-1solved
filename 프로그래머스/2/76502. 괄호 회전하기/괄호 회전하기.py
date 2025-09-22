def is_right(list_s):
    stack = []
    
    if "(" not in list_s:
        return False
    elif "{" not in list_s:
        return False
    elif "[" not in list_s:
        return False
    
    for i in list_s:
        if i == "[":
            stack.append(i)
        elif i == "(":
            stack.append(i)
        elif i == "{":
            stack.append(i)
        
        elif i == "]" and "[" in stack:
            stack.remove("[")
        elif i == "}" and "{" in stack:
            stack.remove("{")
        elif i == ")" and "(" in stack:
            stack.remove("(")
    
    if len(stack) ==0:
        return True
    else:    
        return False


def solution(s):
    answer = 0
    
    list_s = list(s)
    
    for i in range(len(s)):
        if is_right(list_s):
            answer +=1
        
        first = list_s.pop(0)
        list_s.append(first)
        
    return answer