def solution(N, stages):    
    # 실패율 = 스테이지에 도달했으나 아직 클리어 못한 수 / 스테이지에 도달한 플레이어수
    result = []
    player_cnt = len(stages) #분모
    for n in range(N):
        p = stages.count(n+1)
        if p == 0:
            result. append(((n+1),0))
        elif player_cnt>0:
            result.append((n+1,(p / player_cnt)))
            player_cnt -= p
    # print(result)    
    result = sorted(result, key=lambda x: ((-x[1], x[0])))
    
    answer=[]
    for i in result:
        answer.append(i[0])
    # print(result)        

    return answer