m = int(input())

n=1000-m

a = n//500
n = n- (a*500)

b= n//100
n=n-(b*100)

c= n//50
n=  n - (c*50)

d= n//10 
n = n-(d*10)

e = n//5
n = n-(e*5)


answer = a+b+c+d+e+n
print(answer)