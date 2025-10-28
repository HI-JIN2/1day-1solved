from collections import deque

def solution(maps):
    answer = 0
    
    m = len(maps[0])
    n = len(maps)
    
    #동서남북
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    is_right = 0 
    

    queue = deque()
    queue.append((0,0))

    while queue:
        y,x = queue.popleft()
        # print("현재위치",x,y)
        # maps[y][x] = 0 #방문처리

        for i in range(4):
            # print(i)
            nx = x+ dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue

            if maps[ny][nx] ==0: #못가
                continue

            if maps[ny][nx] == 1:
                # print("갈거야",nx,ny)
                # print(maps[ny][nx],maps[y][x])
            
                maps[ny][nx] = maps[y][x]+1
                queue.append((ny,nx))
                
    
    # print(maps)
    
    if maps[n-1][m-1] == 1:
        return -1
    
    return maps[n-1][m-1]