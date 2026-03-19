from collections import deque
# 덱

answer = []

n = int(input())
balloons = list(map(int,input().split()))

# print(n,balloons)
dq = deque()

for i,b in enumerate(balloons):
    dq.append((i+1,b))

# 초기값 맨처음 풍선
i,b = dq.popleft()
now = i
answer.append(i)

while dq:
    if b>0:
        for _ in range(b-1):
            dq.append(dq.popleft())
        i, b = dq.popleft()
        answer.append(i)
    else:
        for _ in range(abs(b)):
            dq.appendleft(dq.pop())
        i, b = dq.popleft()
        answer.append(i)

for a in answer:
    print(a, end = " ")
