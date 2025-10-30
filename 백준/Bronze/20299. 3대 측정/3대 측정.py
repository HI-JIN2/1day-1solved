import sys
input = sys.stdin.readline

n,k,l = map(int,input().split())
member = []

for i in range(n):
    a,b,c =  map(int,input().split())
    if a+b+c>= k  and (a>=l and b>=l and c>=l):
        member.append(a)
        member.append(b)
        member.append(c)

print(len(member)//3)
for m in member:
    print(m,end=" ")