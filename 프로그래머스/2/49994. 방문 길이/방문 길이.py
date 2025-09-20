def solution(dirs):
    result =0
    answer = set()
    x=0
    y=0
    newx=0
    newy=0
    for i in dirs:
        if i=="R":
            newx=x+1
            if -5 <= newx <6:
                answer.add((x,y,newx, y))
                answer.add((newx, y,x,y))
                x=newx
                
        elif i =="L":
            newx=x-1
            if -5 <=newx <6:
                answer.add((x,y,newx, y))
                answer.add((newx, y,x,y))
                x=newx
        elif i =="U":
            newy=y+1
            if -5 <=newy <6:
                answer.add((x,y,x, newy))
                answer.add((x,newy,x,y))
                y=newy
        elif i =="D":
            newy=y-1
            if -5 <=newy <6:
                answer.add((x,y,x, newy))
                answer.add((x,newy,x,y))
                y=newy
            
    print(answer) 
    return len(answer)/2