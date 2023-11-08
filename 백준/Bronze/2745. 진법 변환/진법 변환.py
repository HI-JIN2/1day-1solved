import math

a,b=input().split()
b=int(b)

k=0
result=0
for i in reversed(a):
  # print(i)
  # print(type(i))
  # print(ord(i))
  if ord(i)-55>=10: # A가 기준 
    i=ord(i)-55
  else:
    i=int(i)
    
  result = result + i * math.pow(b,k)
  k=k+1
print(int(result))