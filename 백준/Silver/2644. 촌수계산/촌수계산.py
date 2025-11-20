from collections import deque
n = int(input())
a,b= map(int,input().split()) #촌수를 계산해야하는 번호
m = int(input()) #부모 자식들간의 관계의 개수

graph = [ [ ] for _ in range(100+1)]
visited = [ 0  for _ in range(100+1)]
# print(graph)

# graph = list(map(int,input().split()))
for _ in range(m):
    x,y= map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
# print(graph)

def bfs(s):
    answer = 0
    queue = deque()
    queue.append(s)

    while queue:
        j = queue.popleft()
        # print(j,"===")

        for i in graph[j]:
            # print(i)
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[j] +1
    else:
        return -1


bfs(a)

if visited[b]>0:
    print(visited[b])
else:
    print(-1)