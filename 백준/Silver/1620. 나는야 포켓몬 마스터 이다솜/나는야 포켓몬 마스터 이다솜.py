import sys
from collections import deque

n, m = map(int,input().split())

dq = deque()
dict = {}

for i in range(n):
    name = sys.stdin.readline().strip()
    dq.append(name)
    dict[name]= i+1
# print(dict)

for i in range(m):
    quiz = sys.stdin.readline().strip()
    if quiz.isdigit():
        print(dq[int(quiz)-1])
    else:
        print(dict[quiz])
