
sugar = int(input())
bag =0 

while sugar>=0:
  if(sugar%5 == 0):
    cnt = sugar//5
    bag = bag + cnt
    print(bag)
    break
  sugar = sugar -3
  bag = bag +1
else:
  print(-1)