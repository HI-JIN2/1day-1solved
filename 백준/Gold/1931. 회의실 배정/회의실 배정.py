n = int(input())
data = [ list(map(int,input().split())) for _ in range(n)]

data.sort(key = lambda x: (x[1], x[0]))

# print(data)
answer = 0

now = 0
for t in data:
    start, end = t

    if now <=start:
        answer+=1
        now = end

print(answer)