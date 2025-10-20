from collections import deque

def min_delivery_time(a, b, grid):
    n, m = len(grid), len(grid[0])
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    # 창고, 집 위치 찾기
    warehouse = None
    houses = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                warehouse = (i, j)
            elif grid[i][j] == 2:
                houses.append((i, j))

    # BFS로 최단 거리 계산
    def bfs(start, goal):
        q = deque([(start[0], start[1], 0)])
        visited = [[False]*m for _ in range(n)]
        visited[start[0]][start[1]] = True

        while q:
            x, y, d = q.popleft()
            if (x, y) == goal:
                return d
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if grid[nx][ny] in (1, 2, 3):
                        visited[nx][ny] = True
                        q.append((nx, ny, d + 1))
        return None

    # 각 집까지 거리 계산
    distances = []
    for house in houses:
        dist = bfs(warehouse, house)
        if dist is not None:
            distances.append(dist)

    if not distances:
        return 0  # 배달 불가

    # 가까운 집부터 순서대로 배달
    distances.sort()

    total_time = 0
    for d in distances[:-1]:
        total_time += d * (a + b)  # 왕복
    total_time += distances[-1] * b  # 마지막 집은 편도만 (짐을 들고 감)

    return total_time

a = 10
b = 20
grid = [
    [2,2,0,0,0],
    [0,3,1,0,0],
    [0,0,3,3,2],
    [0,0,3,0,0],
    [0,0,0,2,0]
]
print(min_delivery_time(a, b, grid))  # 210

a = 10
b = 20
grid = [
    [2,0,2],
    [0,1,0],
    [2,0,2]
]
print(min_delivery_time(a, b, grid))  # 0
