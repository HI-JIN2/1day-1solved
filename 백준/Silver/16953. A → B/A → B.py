from collections import deque

a,b = map(int,input().split())

answer =0

queue = deque()
queue.append((a,1))

while queue:
    x, cnt = queue.popleft()
    if x == b:
        break
    for i in (x*2, int(str(x)+'1')):
        # print(i)
        if (i ==b):
            print(cnt+1)
            exit()
        elif(i>b):
            continue
        else:
            queue.append((i, cnt+1))
else:
    print(-1)