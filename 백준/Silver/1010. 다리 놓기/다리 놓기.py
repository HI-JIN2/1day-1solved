import math

a=int(input())

for _ in range(a):
  n,m = map(int,input().split())
  result = math.factorial(m)//(math.factorial(n) *math.factorial(m-n))
  print(result)