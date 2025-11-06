# dp
# 1. 최적부분구조
# 2. 중복되는 부분문제


n = int(input())
array = list(map(int,input().split()))

d = [0]*100 #dp테이블

#바텀업
d[0] = array[0]
d[1] = max(array[0],array[1])

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])


# 4
# 1 3 1 5