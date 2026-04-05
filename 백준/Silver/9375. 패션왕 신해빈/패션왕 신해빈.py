# 그리디
import math

t = int(input()) #테스트 케이스 개수
for _ in range(t):
    answer = 1
    # multiple =  1

    clothes = dict()

    n = int(input())
    for _ in range(n):
        c, t = map(str, input().split())
        if t in clothes:
            clothes[t]+=1
        else:
            clothes[t] = 1
    # print(clothes)

    for c in clothes.values():
        # print(c)
        answer *= (c+1)


    print(answer-1) #알몸인 경우를 제외해야해서 -1

# 1
# 5
# hat headgear
# sunglasses eyewear
# turban headgear
# mask face
# sunglasses face
# makeup face