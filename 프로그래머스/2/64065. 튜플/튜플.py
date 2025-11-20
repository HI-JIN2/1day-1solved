def solution(s):
    answer = []
    l = [ ]
    
    s = s[1:-1]
    s = list(s)
    # print(s)

    stack = []
    isstack = 0
    tmp = ""
    for i in s:
        # print(tmp)
        if i == "{":
            isstack = 1
        elif i == "}":
            stack.append(int(tmp))
            l.append(stack) 
            # print("옮겨")
            isstack = 0 
            stack = []
        elif isstack == 1 and i == ",":
            # print("왜dndhkd")
            # print(tmp)
            stack.append(int(tmp))
            tmp = ""
        elif isstack == 0 and i == ",":
            # print("여긴뎅")
            # stack.append(int(tmp))
            tmp = ""
            
        elif i != ",":
            tmp += i
            # stack.append(i)
        
    # print(l)
    
    
    # l = list(map(l,int))
            
    l.sort(key = lambda x: len(x))
    # print(l)
    
    
    for j in l:
        for k in j:
            if k not in answer:
                answer.append(k)
            
            
     
    return answer