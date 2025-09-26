from collections import deque

graph = {
    1: [4,5],
    2: [3],
    3: [],
    4: [2,3],
    5: [4]
}


def bfs(start_node):
    visited = [False] * (len(graph) +1)

    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        print(node)

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(1)