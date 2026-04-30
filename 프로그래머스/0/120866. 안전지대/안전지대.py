def solution(board):
    answer = 0
    no = [] #지뢰저장소
    x = len(board)
    
    for i in range(x):
        for j in range(x):
            if board[i][j] == 1: #지뢰
                no.append((i,j))
    if len(no) == 0:
        return x*x
    if len(no) == x*x:
        return 0
    
    for n in no:
        #좌우양옆대각선 총 8개
        for dx, dy in [ (1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
            nx = dx+ n[0]
            ny = dy + n[1]
            
            if nx<0 or nx>=x or ny<0 or ny>=x:
                continue
            
            board[nx][ny] = 1
    # print(board)
    
    for i in board:
        for j in i:
            if j == 0:
                answer+=1
    return answer