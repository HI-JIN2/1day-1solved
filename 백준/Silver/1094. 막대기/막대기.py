n = int(input())
a_list = [2**i for i in range(7)]
a_list.reverse()

# print(a_list)
cnt = 0
for i in range(len(a_list)):
  if n >= a_list[i]:
    cnt += 1
    n -= a_list[i]
  if n == 0:
    break

print(cnt)
