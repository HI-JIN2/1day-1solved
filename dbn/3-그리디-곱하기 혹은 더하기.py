#곱하기 혹은 더하기
#그리디
S = input()

# 내 풀이
# result = int(S[0])
#
# l = len(S)
# for i in range(1,l):
#     if S[i] ==0 or result ==0:
#         result += int(S[i])
#     else:
#         result *= int(S[i])


# 동빈나 풀이
result = int(S[0])

for i in range(1, len(S)):
    n = int(S[i])
    if n<=1 or result <=1:
        result +=n
    else:
        result *=n

print(result)

#02984 -> 576
#567 -> 210
#파이썬은 수의 범위 제한이 없음
