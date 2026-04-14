import heapq

def solution(k, score):
    answer = []
        
    heap = []

    for s in score:
        heapq.heappush(heap, s)

        if len(heap) > k: 
            heapq.heappop(heap)

        answer.append(heap[0]) #힙은 맨앞 최소값만 지키지, 내부 정렬을 하진 않음
            
    return answer