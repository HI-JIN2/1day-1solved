a,b,c,d,e,f = map(int,input().split())

y = (d*c-a*f) // (d*b-a*e)
if a != 0:
    x = (c-b*y) // a
else:
    x = (f-e*y) //d

print(x,y)