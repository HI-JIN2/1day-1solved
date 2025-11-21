# 가중치가 있는 최단 경로


from collections import deque

t = int(input())

for test_case in range(t):


    n = int(input())
    graph = []
    dist = [[999 for i in range(n)] for i in range(n)]
    for i in range(n):
        graph.append(list(map(int,input().strip())))

    #print(graph)



    def bfs(y,x):
        dist[0][0] = 0
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        queue = deque()
        queue.append((y,x))

        while queue:
            y, x = queue.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue

                #새 좌표+dist가 더 작으면 이걸로 선택
                if dist[y][x] + graph[ny][nx]  < dist[ny][nx]:
                    dist[ny][nx] = dist[y][x] + graph[ny][nx]
                    queue.append((ny,nx))



    bfs(0,0)
    #print(dist)

    print(f"#{test_case+1} {dist[n-1][n-1]}")