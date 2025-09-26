graph = {
    1: [4,5],
    2: [3],
    3: [],
    4: [2,3],
    5: [4]
}

visited = [ False ] * (len(graph) +1)

def dfs(current_node):
    visited[current_node] = True
    print(current_node)

    for i in graph[current_node]:
        if not visited[i]:
            dfs(i)

dfs(1)