import sys

input = sys.stdin.readline

n = int(input())

data = list(set(map(int,input().split())))
data.sort()
x = int(input())

answer =0

left = 0
right = len(data)-1

# 투포인터
while left<right:
    s = data[left]+data[right]
    if s == x:
        answer+=1
        left+=1
        right -=1
    elif s<x:
        left+=1
    else: #s>x:
        right-=1


print(answer)