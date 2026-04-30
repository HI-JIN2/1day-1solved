from collections import deque
def solution(people, limit):
    answer = 0
    
    #최대한 적게 - 그리디
    #그리디는 정렬
    arr = sorted(people, reverse = True) #내림차순으로
    # print(arr)
    arr = deque(arr)
    
    while arr: #무거운 사람 먼저 태워
        i = arr.popleft()
        if arr and i + arr[-1] <= limit: #무거운 지금 사람이랑 맨 마지막 가벼운 사람 더해도 ㄱㅊ은지
            arr.pop()
        answer+=1
    
    return answer