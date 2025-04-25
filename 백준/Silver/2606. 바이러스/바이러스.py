from collections import deque

def dfs(graph, root):
    visited=[]
    need_visited = deque()

    need_visited.append(root)

    while need_visited:
        node = need_visited.pop()

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph.get(node,[]))
    return len(visited)




n=int(input())
m=int(input())
graph=dict()
for i in range(m):
    key, value = map(int,input().split())
    if key not in graph:
        graph[key]=list()
    if value not in graph:
        graph[value]=list()
    
    graph[key].append(value)
    graph[value].append(key) #양방향 연결


answer = dfs(graph, 1)
print(answer -1)

