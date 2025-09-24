def solution(s):    
    stack =[]
    
    s = s.split()

    for i in s:

        if i == "Z" and len(stack) !=0:
            stack.pop()
            continue
        else:
            stack.append(int(i))
    return sum(stack)
