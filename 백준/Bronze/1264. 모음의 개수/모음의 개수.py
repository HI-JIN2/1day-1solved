while True:
  a = input()
  if (a=="#"):
    break
  else: 
    a_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    a_count=0
    for i in a:
      if (i in a_list): 
        a_count+=1
      else:
        continue
    print(a_count)