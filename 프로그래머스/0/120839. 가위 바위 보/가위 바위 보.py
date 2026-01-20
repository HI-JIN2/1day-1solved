def solution(rsp):
    answer = ''
    
    l = list(rsp)
    
    for i in l:
        if i == "2":
            answer+="0"
        elif i == "0":
            answer+="5"
        else:
            answer+="2"
    
    return answer