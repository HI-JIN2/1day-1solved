import math

n, k =map(int,input().split())

fdata = [0]*6
data = [0]*6
answer = 0
for i in range(n):
    s,y = map(int,input().split())
    if s == 0:
        fdata[y-1]+=1
    else:
        data[y-1]+=1

# print(data,fdata)

for d in fdata:
    answer += math.ceil(d/k)

for d in data:
    answer += math.ceil(d/k)

print(answer)