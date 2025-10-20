N=int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))



# # a를 재배열
# a.sort()
# b.sort(reverse=True)

# result =0
# for i in range(N):
#     result+=a[i]*b[i]

result =0
# 재배열 안하도록
for i in range(N):
    result += min(a)*max(b)
    a.pop(a.index(min(a))) #pop은 인덱스로 해야함
    b.pop(b.index(max(b))) # Remove and return item at index (default last).


print(result)