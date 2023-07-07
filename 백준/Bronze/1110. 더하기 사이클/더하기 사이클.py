def new_num(n):
    if n<10:
        a=0
        b=n
        c=a+b
        return b*10+c%10
    else:
        a=n//10
        b=n%10
        c=a+b
        return b*10+c%10

def done(origin):
    num = 1
    n=origin
    while True:
        if origin!=new_num(n):
            n=new_num(n)
            num+=1
        else:
            return num

n=int(input())
print(done(n))