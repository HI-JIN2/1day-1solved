n,m=map(int,input().split())

s=[]

def func(start):
    if len(s)==m:
        print(*s)
        return
    
    else:
        for i in range(start,n+1): #사전순
            if i not in s: #중복 안됨
                s.append(i)
                func(i+1)
                s.pop()

func(1)