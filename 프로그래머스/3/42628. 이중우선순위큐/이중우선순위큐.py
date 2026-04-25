import heapq
def solution(operations):
    answer = []
    heap = [ ]
    
    #기본이 최소힙이므로 최소는 pop으로 하고
    #최대는 max
    for o in operations:
        action, num = o.split()
        if action == "D" and not heap: #힙 비었는지 체크
            pass
        elif action == "D" and num == "-1":
            #최소삭제
            heapq.heappop(heap) #최소값이 자동으로 보장 
        elif action == "D" and num == "1":
            #최대 삭제
            n = max(heap)
            heap.remove(n)
        else: #삽입
            heapq.heappush(heap, int(num))
            
            
    if len(heap) == 0:
        return [0,0]
    else:
        answer.append(max(heap)) #최대
        answer.append(heapq.heappop(heap)) #최소
    
    return answer