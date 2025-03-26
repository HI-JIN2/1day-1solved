N=int(input())
l=list()
for i in range(1,N+1):
    a=int(input())
    l.append(a)

l.sort()

for i in l:
    print(i,sep="\n")
