from collections import deque
import sys

input = sys.stdin.readline

n=int(input()) #100이하 자연수

graph = [list(map(int,input().split())) for i in range(n)]

visited = [[False]*n for _ in range(n)]
# print(graph)


def bfs(x,y):
    q = deque()
    q.append((x,y)) #초기값
    new_island = set() #각 섬에 해당하는 좌표들을 모을것임
    visited[x][y] = True

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x,y = q.popleft()
        new_island.add((x,y))

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0>nx or nx>=n or 0>ny or ny>=n:
                continue #범위 초과

            if graph[nx][ny]==0:
                continue #육지 아니면 더할 필요 없음

            if graph[nx][ny]==1 and not visited[nx][ny]: #육지이고 방문 안한 땅만
                visited[nx][ny] = True #선 방문처리 후 큐에 넣기
                q.append((nx,ny))
    return new_island #1번섬에 해당하는 좌표들을 반환, 2,3번도


#결국은 섬간의 최단거리를 구하는 것이기에 이걸 못만들면 못품
def cal(i,j): #1번섬과 2번섬의 거리
    min_dist = 99999
    i_x = island[i]
    i_y = island[j]

    for x in i_x:
        for y in i_y:
            min_dist = min( min_dist, abs(x[0]-y[0]) + abs(x[1]-y[1]))
    return min_dist



island = [] #각 섬에 해당하는 좌표들을 구분
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]: #육지인데 방문을 안했으면 방문
            new_island = bfs(i,j)
            island.append(new_island)

result = 99999 #가장 짧은 다리의 길이

# print(island)

for i in range(len(island)): #섬끼리의 거리를 비교 1번섬이랑 2번섬, 2번섬이랑 3번섬, 1번섬이랑 3번섬
    for j in range(i+1, len(island)):#이걸로 중복을 제거했더니 시간초과에서 성공으로 바뀜
        if i!=j:
            result = min( result, cal(i,j) -1 )

print(result)
