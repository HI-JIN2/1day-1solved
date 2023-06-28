import sys

N=int(input())
M=[]
for i in range(N):
    a=int(sys.stdin.readline().strip())
    M.append(a)

M=sorted(M)

for i in M:
    print(i)