

n=int(input())
m=int(input())

j=0
for i in range(m):
    a,b=map(int,input().split())
    c=a*b
    j=j+c
        
if j==n:
    print("Yes")
else:
    print("No")
    