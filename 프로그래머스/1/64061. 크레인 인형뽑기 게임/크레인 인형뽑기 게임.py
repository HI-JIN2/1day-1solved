[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]

def solution(board, moves):
    answer = 0
    
    bucket = []
    n = len(board)
    
    for move in moves:
        # print(move,"를 찾아요")
        for i in range(n):
            if board[i][move-1] == 0:
                continue
            else:
                it = board[i][move-1] 
                board[i][move-1]  =0 
                # print(it)
                if len(bucket) != 0 and bucket[-1] == it :
                    bucket.pop()
                    answer +=2
                    break
                else: 
                    bucket.append(it)
                    break

    
    return answer