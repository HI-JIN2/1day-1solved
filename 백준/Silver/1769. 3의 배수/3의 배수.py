a=input()
cnt=0
while len(a)>=2:
  new_a=0
  for i in range(len(a)):
    new_a+=int(a[i])
  # print(new_a)
  a=str(new_a)
  cnt+=1
print(cnt)
if int(a)%3==0:
  print("YES")
else:
  print("NO")
