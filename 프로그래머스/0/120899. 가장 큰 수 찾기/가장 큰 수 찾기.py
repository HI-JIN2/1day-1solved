def solution(array):
    answer = []
    
    answer.append(array[0])
    answer.append(0)
    
    for idx, n in enumerate(array):
        if answer[0]<n:
            answer.pop()
            answer.pop()
            answer.append(n)
            answer.append(idx)
    return answer