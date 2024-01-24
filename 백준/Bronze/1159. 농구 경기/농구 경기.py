n=int(input())
name_list = []
result =[]
for i in range(n):
  name=input()
  name_list.append(name[0])

setlist=set(name_list)

for i in setlist:
  if name_list.count(i) >=5:
    result.append(i)

if len(result)>0:
  print(''.join(sorted(result)))
else:
  print("PREDAJA")