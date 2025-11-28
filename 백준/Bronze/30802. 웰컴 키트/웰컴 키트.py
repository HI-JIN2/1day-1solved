
import math
n = int(input())
tshirts = list(map(int,input().split()))
t, p = map(int,input().split())

answer =0
for s in tshirts:
    answer += ((s//t+1))
    if s%t == 0 :
        answer -= 1
    # print(s, (s//t+1))
print(answer)
das = n//p
print(das, n - das*p)