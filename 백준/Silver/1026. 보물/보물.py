N=int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))



# a를 재배열
a.sort()
b.sort(reverse=True)


result =0
for i in range(N):
    result+=a[i]*b[i]

print(result)