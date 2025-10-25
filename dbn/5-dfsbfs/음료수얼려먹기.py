def dfs(n,m,x,y,graph):
    if x<=-1 or y<=-1 or x>=n or y>=m:
        return False

    if graph[x][y] == 0:
        graph[x][y] =1 #방문처리
        dfs(n,m,x-1,y,graph)
        dfs(n,m,x+1,y,graph)
        dfs(n,m,x,y-1,graph)
        dfs(n,m,x,y+1,graph)
        return True # 할거 다 하고 true 반환하면 이게 하나의 개수로 쳐짐
    return False

def solution(n,m,graph):
    answer =0

    for i in range(n):
        for j in range(m):
            if (dfs(n,m,i,j,graph)) ==True:
                answer +=1
    return answer


graph = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]
print(solution(4,5,graph))
# from dremdeveloper.bfs_queue import graph
#
# n,m=map(int,input().split())
# graph = [
#     [0,0,1,1,0],
#     [0,0,0,1,1],
#     [1,1,1,1,1],
#     [0,0,0,0,0]
# ]
#
# def dfs(x,y):
#     if x<=-1 or y<=-1 or x>=n or y>=m:
#         return False
#
#     if graph[x][y] == 0:
#         graph[x][y] =1 #방문처리
#         dfs(x-1,y)
#         dfs(x+1,y)
#         dfs(x,y-1)
#         dfs(x,y+1)
#         return True
#     return False
#
# def solution(n,m,graph):
#     answer =0
#
#     for i in range(n):
#         for j in range(m):
#             if (dfs(n,m,i,j,graph)) ==True:
#                 answer +=1
#     return answer
#
#
#
# print(solution(4,5,graph))