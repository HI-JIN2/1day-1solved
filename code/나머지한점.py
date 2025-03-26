def solution(v):
    x=[]
    y=[]
    answer =[]
    
    for i in range(3):
        if v[i][0] in x:
            x.remove(v[i][0])
        elif v[i][0] not in x:
            x.append(v[i][0])
        if v[i][1]  in y:
            y.remove(v[i][1])
        elif v[i][1] not in y:
            y.append(v[i][1])

    answer.append(x[0])
    answer.append(y[0])

    return answer