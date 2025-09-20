from collections import deque
def dfs(graph,v):
    visited =[]

    need_visited = deque()

    need_visited.append(v) #루트 부터 시작 

    while need_visited:
        node = need_visited.pop()

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph.get(node,[]))
    return visited

def bfs(graph,v):
    need_visited, visited =[],[]
    need_visited.append(v)

    while need_visited:
        node = need_visited[0]
        del need_visited[0]

        if node not in visited:
            visited.append(node)
            need_visited.extend(graph.get(node,[]))

    return visited




n,m,v = map(int,input().split())
graph = dict()
for i in range(m):
    key, value = map(int,input().split())
    if key not in graph:
        graph[key]=list()
    if value not in graph:
        graph[value]= list()
    graph[key].append(value)
    graph[value].append(key) #양방향 연결 

# print(graph)


# 이걸 왜해야하지?
for key in graph:
    graph[key].sort(reverse=True)
# print(graph)

for i in dfs(graph,v):
    print(i,end=" ")
print()

for key in graph:
    graph[key].sort(reverse=False)
for i in bfs(graph,v):
    print(i,end=" ")
