from collections import deque
import sys

n = int(sys.stdin.readline())
q = deque()

for i in range(n):
  a = sys.stdin.readline().split()
  if a[0] == 'push':
    # print(a[1])
    q.append(int(a[1]))
  elif a[0] == 'pop':
    if len(q) == 0:
      print(-1)
    else:
      print(q[0])
      q.popleft()
  elif a[0] == 'size':
    print(len(q))
  elif a[0] == 'empty':
    if len(q) == 0:
      print(1)
    else:
      print(0)
  elif a[0] == 'front':
    if len(q) == 0:
      print(-1)
    else:
      print(q[0])
  elif a[0] == 'back':
    if len(q) == 0:
      print(-1)
    else:
      last = len(q)
      print(q[last - 1])
