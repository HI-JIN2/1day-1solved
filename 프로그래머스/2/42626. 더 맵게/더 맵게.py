import heapq

def solution(scoville, K):
    answer = 0
    # heap = []
    
    heapq.heapify(scoville)
    
    
    while True:

        if scoville[0]>=K:
            return answer
        elif len(scoville)<=1:
            return -1
        else:
            x = heapq.heappop(scoville)
            y= heapq.heappop(scoville)
            heapq.heappush(scoville,x+ y*2)            
        
            answer+=1
    return answer