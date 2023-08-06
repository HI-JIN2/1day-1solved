N,M=map(int,input().split())
bucket=[]

for i in range(1,N+1):
    bucket.append(0)

# print(bucket)

for _ in range(M):
    i,j,k=map(int,input().split())
    for i in range(i,j+1):
        bucket[i-1]=k
    # print(bucket)

for i in range(N):
    print(bucket[i],end=" ")
# print(bucket)