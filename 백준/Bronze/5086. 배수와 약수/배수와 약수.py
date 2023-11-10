n, m = map(int, input().split())

while (True):
  if (n == 0 & m == 0):
    break
  else:
    if (n % m == 0):
      print("multiple")
    elif (m % n == 0):
      print("factor")
    else:
      print("neither")
    n, m = map(int, input().split())
