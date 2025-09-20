def solution(id_list, report, k):
    # 신고당한 횟수 
    goal = { i:0 for i in id_list } #id_list만큼 0으로 채움 신고한 
    
    # 신고한 횟수 
    real = {i:set() for i in id_list }


    for i in set(report): #같은 사람이 같은 사람 신고한건 포함이 안되서 set
        a,b = i.split()
        real[a].add(b) #a가 신고한 목록에 b를 추가
        goal[b]+=1 #b가 신고당한 횟수 1증가
    
    result = []
    for i in real: #신고한 횟수 리스트도 id리스트 기반임 순서 같음
        count =0
        for j in real[i]: #i씨가 신고한 리스트 중에 꺼내쓰기 
            if goal[j] >=k:
                count +=1
        result.append(count) 
        
    return result