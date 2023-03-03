while True:
    a,b,c=map(int,input().split())
    if(a==0&b==0&c==0):
        break
    elif( c*c == a*a + b*b):
        print("right")
        continue
    elif( a*a==b*b+c*c):
        print("right")
        continue

    elif(b*b == c*c +a*a):
        print("right")
        continue
    else:
        print("wrong")
        continue