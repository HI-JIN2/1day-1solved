def solution(plans):
    answer = []
    stack = []
    
    for p in plans:
        h, m = map(int,p[1].split(":"))
        m += h*60
        p[1]=m
        
    # print(plans)
    
    # 시작 시간으로 정렬
    plans.sort(key = lambda x: x[1])
    # print(plans)
    
    
    now = 0 
    
    for i in range(len(plans)-1):
        
        name, start, playtime = plans[i]
        playtime = int(playtime)
        nextstart = int(plans[i+1][1])
        
        if start+playtime <= nextstart:
            answer.append(name)#이건 stack에 넣을 필요가 없음
            
            #그 이후까지 시간이 뜬다면? 
            temp = nextstart-(start+playtime) #남는 시간 
            # print(name,temp,stack)
            
            while temp>0 and stack :
                name, time = stack.pop()
                # print(name,time)
                if temp-time >=0: #남은 시간동안 과제 다 할 수 있으면
                    # print("can")
                    answer.append(name)
                    temp = temp-time
                else:
                    # print("e")
                    lasttime = time-temp
                    # print(lasttime)
                    stack.append((name,lasttime ))
                    temp = 0
                # print(temp)
               
        else: #다음 시간까지 못했다면 stack에 넣어야함
            stack.append((name, playtime - (nextstart - start)))
            
    
    #마지막 타임 체크
    answer.append(plans[-1][0])
    
    #그 이후 스택에 남은거 체크
    while stack:
        name, time = stack.pop()
        answer.append(name)
            
    
    return answer