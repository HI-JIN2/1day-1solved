def solution(emergency):
    answer = [0]*len(emergency)
    
    l = []
    
    for i, e in enumerate(emergency):
        l.append((i+1,e))
    
    l = sorted(l, key = lambda x: x[1], reverse = True)
    # print(l)
    
    for i, (num, e) in enumerate(l):
        answer[num-1] = i+1
    return answer