def solution(numbers):
    answer = [-1]*len(numbers)
    
    # 시간초과 안날려면 스택을 쓰라 
    stack = [] #아직 큰수 못찾은 인덱스를 저장하는 스택
    
    for i, n in enumerate(numbers):
        # 이전에 봤던 숫자 중에서 아직 답을 못찾은 애가 있고 = 스택이 안비었고
        # 그 애보다 현재 숫자가 크면 현재 숫자가 그 애의 큰수이다. 
        while stack and numbers[stack[-1]] <n:
            idx = stack.pop()
            answer[idx] = n
        
        stack.append(i) #스택에 저장하는건 인덱스임. 정답 못찾은 인덱스
    
    
    return answer