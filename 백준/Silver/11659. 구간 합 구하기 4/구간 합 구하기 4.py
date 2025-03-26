import sys
input = sys.stdin.readline
# s[j]-s[i-1]
n,m=map(int,input().split())
number = list(map(int,input().split()))
구간합 = [0,]
temp=0

for i in number:
    temp = temp + i
    구간합.append(temp)

for i in range(m):
    a,b=map(int,input().split())
    print(구간합[b]-구간합[a-1])
