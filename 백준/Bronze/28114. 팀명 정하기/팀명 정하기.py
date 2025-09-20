import sys
input = sys.stdin.readline

year = []
ys = ""

n = dict()


for i in range(3):
  a,b,c = input().split()
  # print(a,b,c)
  y = b[2:]
  year.append(int(y))
  n[c] = int(a)


year.sort()
for i in year:
  ys=ys+str(i)
print(ys)

sorted_dict = sorted(n.items(), key= lambda item:item[1], reverse=True)

# print(sorted_dict)
print(sorted_dict[0][0][0], sorted_dict[1][0][0],sorted_dict[2][0][0], sep="")


