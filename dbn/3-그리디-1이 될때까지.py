#N이 1이 될때까지

n,k=map(int,input().split())
cnt =0

# 내 풀이
# while n>1:
#     if n%k==0: #나누어 떨어지면 최대한 나눠야함 = 그리디
#         # print(n,k,n%k)
#         n = n//k
#         cnt+=1
#     else:
#         # print(n,n-1)
#         n= n-1
#         cnt +=1

# 동빈나 풀이
# 이게 O(logN)
while True:
    target = (n//k)*k
    cnt += (n-target)

    n = target

    if n<k:
        break
    cnt +=1
    n //=k

cnt += (n-1)


print(cnt)

# n이 아무리 커도 k로 계속 나누면 빠르게 줄일 수 있음


# 25 5=>2
# 25 3 ->6


