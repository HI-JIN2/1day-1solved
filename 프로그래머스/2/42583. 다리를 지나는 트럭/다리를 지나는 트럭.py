from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    now_weight = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    while trucks or now_weight > 0:
        out = bridge.popleft()
        now_weight -= out

        if trucks:
            now = trucks.popleft()

            if now_weight + now <= weight:
                bridge.append(now)
                now_weight += now
            else:
                bridge.append(0)
                trucks.appendleft(now)
        # else:
        #     bridge.append(0)
           
        answer+=1
    return answer