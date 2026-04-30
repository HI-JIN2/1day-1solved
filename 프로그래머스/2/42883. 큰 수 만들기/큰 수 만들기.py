def solution(number, k):
    answer = ''
    stack = []
    
    d = k
    for n in number:
    
        while stack and stack[-1]<n and d>0:
            stack.pop()
            d-=1  #이 문제의 그리디함은 여기서 나온다. 앞부터 뺄 수 있는 거 빼
        
        stack.append(n)
        # print(stack, d)

    if d>0:
        stack=stack[:-d]
            
        
    return "".join(stack)