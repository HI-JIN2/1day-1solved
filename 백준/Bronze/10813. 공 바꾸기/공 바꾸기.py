N, M = map(int,input().split())

bucket=[]

for i in range(1,N+1):
    bucket.append(i)
# print(bucket)

for _ in range(M):
    i, j = map(int,input().split())
    temp=bucket[i-1]
    bucket[i-1]=bucket[j-1]
    bucket[j-1]=temp

for i in range(N):
    print(bucket[i], end=" ")