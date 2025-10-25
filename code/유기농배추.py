import sys
sys.setrecursionlimit(10000)
from sys import stdin
input = stdin.readline

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    def dfs(x, y): #재귀
        graph[y][x] = 0  # 시작점 방문 처리

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[ny][nx] == 0:
                continue

            if graph[ny][nx] == 1:
                # graph[ny][nx] = 0  # 방문처리 안해도 됨
                dfs(nx,ny)

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        graph[y][x] = 0 #시작점 방문처리

        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx<0 or nx>=m or ny<0 or ny>=n:
                    continue

                if graph[ny][nx]:
                    graph[ny][nx] = 0 #방문처리
                    queue.append((nx,ny))



    answer = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                # dfs(x, y)
                bfs(x,y)
                answer += 1
    print(answer)