from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    result = [] #탐험 횟수를 기록
    
    # 던전의 순열 (순서가 있는 나열)
    for p in permutations(dungeons):
        # print(p)
        cost = k
        cnt = 0 
        for i in p:
            if cost>=i[0]: #현재 피로도가 최소 피로도 이상이어야 갈 수 있음
                cost-=i[1] #가면 소모피로도가 깎임
                cnt+=1 #방문 던전 하나 적립
        result.append(cnt) 
                
                

    
    return max(result)