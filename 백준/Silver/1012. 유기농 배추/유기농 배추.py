import sys
sys.setrecursionlimit(10000)
from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    def dfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        graph[y][x] = 0  # 방문 처리

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                dfs(nx, ny)

    answer = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                dfs(x, y)
                answer += 1
    print(answer)