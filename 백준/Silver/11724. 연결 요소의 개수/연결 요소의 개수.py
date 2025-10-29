from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[  ] for i in range(n+1)]
# print(graph)

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u) #양방향 연결


# print(graph)
visited = [False] * (n+1)

def bfs(start):
    queue = deque()
    queue.append(start)

    while queue:
        x = queue.popleft()
        visited[x] = True

        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return

total = 0
for i in range(1,n+1):
    if not visited[i]: #bfs로 못잡아 낸 것만 여기서 도는거라서 카운팅 하면 됨
        # print(i)
        bfs(i)
        total +=1

print(total)