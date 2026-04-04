n = int(input())
pat = input()
files = [ input() for i in range(n)]

# print(files)

first, last = pat.split("*")

for f in files:
    if len(f)< len(first)+len(last):
        print("NE")
    elif f.startswith(first) and f.endswith(last):
        print("DA")
    else:
        print("NE")