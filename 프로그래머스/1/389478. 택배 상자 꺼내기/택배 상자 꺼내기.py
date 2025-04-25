def solution(n, w, num):
    answer = 0
    
    if w==1:
        return n-num+1
   
    # height = n//w
    # f = num // w  #몇층인지
    # print(height,f)
    # if n%w==0:
    #     return height - f +1
    
    height = n//w
    if(n%w!=0):
        height+=1
    print("총 높이",height)

    
    f = num // w  #몇층인지
    if(num%w!=0):
        f+=1
    print("f는 ",f) #num이 2층에 있다는걸 알았음
    
    
    if n%w==0:
        return height - f +1
    #그층이 몇갠지 
    #몇번째 위치인지
    my = num%w 
    if f %2==0:
        #<-방향
        if(my==0):
            print("오른쪽에서",w)
            my=w
        else:
            print("오른쪽에서",my)
    else: 
        # -> 방향
        if(my==0):
            print("왼쪽에서",w)
            my=w
        else:
            print("왼쪽에서",my)
    
    
    #마지막줄의 방향 
    if height %2 ==0:
        #<- 방향이에요
        print(n%w, "<-방향으로 몇개")
    else: 
        # -> 방향이에요 
        print(n%w,"->방향으로 몇개")
    top=n%w
    
    
    #방향이 다르면 
    a= height %2
    b=f %2
    
    answer = height-f 

    
    #방향이 같으면 
    if (a==0 and b==0 ) or (a==1 and b==1):
        print(a,b)
        if top - my>=0:
            answer +=1  
    #방향이 다르면 
    else: 
        print(a,b)
        if top-(w-my)>=0:
            answer +=1


    # answer = height-f +1
        
    
    
    
    
    return answer