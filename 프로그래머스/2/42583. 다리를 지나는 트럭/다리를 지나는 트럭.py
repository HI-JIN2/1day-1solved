from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    now_weight = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    while trucks or now_weight > 0: #가야하는 차가 남았거나 다리 위의 차가 남은 동안
        out = bridge.popleft()
        now_weight -= out

        if trucks:
            now = trucks.popleft()

            if now_weight + now <= weight: 
                bridge.append(now)
                now_weight += now 
            else:
                bridge.append(0) #차 대신 0 추가
                trucks.appendleft(now) #아까 뽑은거 다시 대기열에 추가
 
        answer+=1 #1초씩 증가
    return answer
