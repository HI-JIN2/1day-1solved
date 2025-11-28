from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
queue = deque()
for test_case in range(t):
    n = input().strip()
    # print(n)
    if n.startswith("push"):
        n = n.split()
        queue.append(n[1])
    elif n == "front":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif n == "back":
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
    elif n == "size":
        print(len(queue))
    elif n == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif n == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
