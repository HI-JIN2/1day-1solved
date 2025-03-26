import sys
input = sys.stdin.readline
n,m=map(int,input().split())
t=[]
jj=[0]*n
hap = [jj,]
temp =0

for i in range(n):
    t.append(list(map(int,input().split())))

for i in range(n):
    합 = [0,]
    for j in t:
        temp +=j[i]
        합.append(temp)
    hap.append(list(합))
    temp =0


for i in range(m):
    a,b,c,d=map(int,input().split())

    r= hap[a][d]
    x=hap[a][b-1]
    y= hap[c][d]
    z=hap[c][b-1]

    # print("\n")
    if (a==b) & (b==c) &(c==d) &(d==a):
        print(t[a-1][b-1])
    elif (a==c) & (b==d):
        # print("(a==c) & (b==d")
        print(t[a-1][b-1])
    elif (a==b) & (c==d):
        # print("(a==b) & (c==d)")
        print((r-x + y-z)*2)
    else: 
        print(r-x + y-z)
