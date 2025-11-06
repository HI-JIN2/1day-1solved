n,m = map(int,input().split())
#화폐 개수, 만들 수

array = []
for i in range(n):
    array.append(int(input()))
array.sort()

d = [10001] * (m+1)


#바텀업 방식으로 생각
# for j in array:
#     for i in range(j,m+1):
#         if i%j == 0:
#             d[i] = i//j #나누어 떨어지면 그 몫을 넣어
#         d[i] = min(d[i], d[i-j]+1)
#     print(j, d)

#정답 풀이
d[0] =0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j - array[i]] != 10001: # i-k원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j -array[i]]+1)
    print(i, d)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])