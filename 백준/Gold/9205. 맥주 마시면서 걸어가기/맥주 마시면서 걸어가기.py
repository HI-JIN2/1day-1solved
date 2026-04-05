from collections import deque

t = int(input())


def cal(x,y, nx, ny):
    return abs(x-nx) + abs(y-ny)

# 맥주는 50미터를 가기 전마다 마셔야하고
# 한박스 max 20개까지 채울 수 있음




for _ in range(t):
    n = int(input())

    l = []

    hx,hy =(map(int,input().split()))
    l.append((hx,hy))

    for _ in range(n):
        x,y = map(int,input().split())
        l.append((x,y))

    ex,ey = map(int,input().split())
    l.append((ex,ey))

    # print(l)
    can = True


    def bfs():
        q = deque()
        visited = [False] * len(l)
        visited[0] = True
        q.append(l[0])

        while q:
            x,y = q.popleft()

            #남은 좌표들이랑 비교를 해야하는데
            for i, (nx,ny) in enumerate(l):
                if not visited[i] and cal(x,y, nx, ny)<=1000: #방문 안했고 1000미터 내면
                    visited[i] = True
                    q.append((nx,ny))
        if visited[-1]:
            print("happy")
        else:
            print("sad")

    bfs()