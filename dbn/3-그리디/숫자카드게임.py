n,m = map(int,input().split())
result = 0
l = []

for i in range(n):
    data = list(map(int,input().split()))
    l.append(min(data))

l.sort()

print(l[-1])

#3 3
# 3 1 2
# 4 1 4
# 2 2 2
# => 2

# 2 4
# 7 3 1 8
# 3 3 3 4
# => 3
