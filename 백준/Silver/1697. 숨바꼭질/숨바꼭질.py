from collections import deque

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == k:
            print(dist[k])
            break
        for nx in (x-1, x+1, x*2):
            if nx<0 or nx>MAX:
                continue

            if not dist[nx]: #x=5면 nx는 4,6,10. 이미 값이 있는건 안감
                # print(x,dist[x])
                dist[nx] = dist[x]+1
                queue.append(nx)

MAX = 100000
dist = [0] * (MAX+1)
n,k = map(int,input().split())
bfs()