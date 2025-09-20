n=int(input())

if n%10 !=0:
    print(-1)
else:

    a = n//(60*5)
    n = n- (a*60*5)

    b =n //60
    n= n-b*60

    c = n//10
    n = n- c*10

    print(a,b,c)