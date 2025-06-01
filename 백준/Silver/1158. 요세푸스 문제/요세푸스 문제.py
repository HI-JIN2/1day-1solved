from collections import deque

n, k = map(int, input().split())
d = deque()
for i in range(n):
  d.append(i + 1)

result = []


while d:
  for _ in range(k-1):
    d.append(d.popleft())

  result.append(d.popleft())

print(str(result).replace('[', '<').replace(']', '>'))