import heapq
def solution(scoville, K):
    answer = 0
    
    # 모든  음식이 스코빌 지수 k 이상
    
    # 섞은 스코빌 = 안매운+두번째로 안매운 *2
    
    #최소힙을 쓰면 연산회수가 줄겠지?
    
    heapq.heapify(scoville)
    while scoville:
        if scoville[0]>=K:
            return answer
        elif len(scoville)<=1: #원소가 2개는 있어야 할 수 있음 
            return -1
        elif scoville[0]<K:
            m1 = heapq.heappop(scoville)
            m2 = heapq.heappop(scoville)
            new = m1+ m2*2
            heapq.heappush(scoville,new)
            answer+=1 
    
    return answer