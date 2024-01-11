import sys

a = int(sys.stdin.readline().rstrip())

#a = 5

cnt=2
for _ in range(a):
  cnt = cnt + cnt-1

print(cnt**2)
