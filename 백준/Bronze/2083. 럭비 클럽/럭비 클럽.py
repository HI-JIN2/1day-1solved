while True:
  a,b,c = map(str,input().split())
  b = int(b)
  c = int(c)
  if (a=="#"):
    break
  elif (b>17) |(c>=80):
    print(f"{a} Senior")
  else: 
    print(f"{a} Junior")
    
