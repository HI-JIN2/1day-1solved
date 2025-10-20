# 내 풀이
# l = [2,4,5,4,6]
#
# m =8
# k =3
#
# l.sort(reverse=True)
# print(l)
#
# result =0
# cnt =0
# for _ in range(m):
#     if cnt < k:
#         result += l[0]
#         print(l[0])
#         cnt +=1
#     else:
#         result += l[1]
#         print(l[1])
#         cnt =0

# 동빈나 풀아
n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result =0
# while True:
#     for i in range(k):
#         if m ==0 :
#             break
#
#         result += first
#         m-=1
#     if m ==0:
#         break
#     result += second
#     m-=1


# 더 개선
count = int(m/(k+1))*k
count += m % (k+1)

result += (count) * first
result += (m-count ) * second

print(result)