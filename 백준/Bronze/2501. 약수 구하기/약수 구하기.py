n,m=map(int,input().split())

n_list=[]

for i in range(1,n+1):
  if n%i==0:
    n_list.append(i)

if m > len(n_list):
  print(0)
else:
  print(n_list[m-1])