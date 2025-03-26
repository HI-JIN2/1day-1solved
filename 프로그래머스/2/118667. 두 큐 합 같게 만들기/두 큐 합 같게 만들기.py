from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum1 = sum(q1)
    sum2=sum(q2)
    
    while True:
        
        if answer == 4*len(queue1): #어떤 경우에도 안됨
            return -1 

        if sum1 > sum2:
            # print("1이 더 커")
            temp = q1.popleft()
            q2.append(temp)
            sum1-=temp
            sum2+=temp
        elif sum1 < sum2:
            # print("2이 더 커")
            temp = q2.popleft()
            q1.append(temp)
            sum1+=temp
            sum2-=temp
        else: 
            print("끝")
            return answer
        answer+=1