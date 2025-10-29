from collections import deque

n, w, l = map(int,input().split())
#트럭수 , 다리길이, 최대하중

trucks = list(map(int,input().split()))
trucks = deque(trucks)

bridge = deque([0]*w) #다리

time = 0

while bridge: #다리가 다 비면 종료
    time+=1 #다리에 차량이 있는 시간을 카운트
    bridge.popleft()

    # print(time, bridge,trucks)
    if trucks:
        if sum(bridge)+trucks[0]<=l: #하중이 될때는 다리에 올리고
            x = trucks.popleft()
            bridge.append(x)
        else: #하중이 안될때는 0을 올림
            bridge.append(0)
print(time)

