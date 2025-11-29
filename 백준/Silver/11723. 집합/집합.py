from collections import deque
import sys

input = sys.stdin.readline
all_numbers = [i for i in range(1,20+1)]

t = int(input())
queue = deque()
for test_case in range(t):
    s = input().strip()

    if s.startswith("add"):
        n = s.split()
        if int(n[1]) not in queue:
            queue.append(int(n[1]))
    elif s.startswith("remove"):
        n = s.split()
        if int(n[1]) in queue:
            queue.remove(int(n[1]))
    elif s.startswith("check"):
        n = s.split()
        if int(n[1]) in queue:
            print(1)
        else:
            print(0)
    elif s.startswith("toggle"):
        n = s.split()
        if int(n[1]) in queue:
            queue.remove(int(n[1]))
        else:
            queue.append(int(n[1]))
    elif s == "all":
        queue.clear()
        queue = deque(all_numbers)
    elif s == "empty":
        queue.clear()