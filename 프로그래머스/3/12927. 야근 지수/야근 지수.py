import heapq

def solution(n, works):
    answer = 0
    
    heap = [-w for w in works]
    heapq.heapify(heap)

    for _ in range(n):
        x = heapq.heappop(heap)   # 가장 큰 값
        
        if x == 0:   # 이미 전부 0이면 더 줄일 필요 없음
            heapq.heappush(heap, x)
            break

        heapq.heappush(heap, x + 1)
    
    for i in heap:
        answer+=i**2
    
    return answer