def solution(X, Y):

    l = []
    
    X = list(map(int,X))
#     X.sort()
    
    Y = list(map(int,Y))
#     Y.sort()
    
    #공통의 정수를 뽑아내야함
    # for x in X:
        # if x in Y: # in이 비싸다 
            # l.append(x)
            # Y.remove(x)
            
    xl = [0]*10
    yl = [0]*10
    for x in X:
        xl[x]+=1
    for y in Y:
        yl[y]+=1
    # print(xl,yl)
        
    for i in range(10):
        cnt = min(xl[i],yl[i])
        for _ in range(cnt):
            l.append(i)
            
    l.sort(reverse=True)
    # print(l)
    
    if len(l)==0:
        return "-1"
    elif l[0] == 0:
        return "0"
    return "".join(list(map(str,l)))
