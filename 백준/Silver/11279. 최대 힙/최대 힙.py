import heapq
import sys

input = sys.stdin.readline

t = int(input())
arr = []
for i in range(t):
    x = int(input())
    if x==0:
        if arr:
            print(-heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr,-x)