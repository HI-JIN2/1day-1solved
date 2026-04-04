data = input()
stack = []
answer = 0

for i in range(len(data)):
    if data[i] == '(': #한번에 잘리는 막대기의 수를 더해나감
        stack.append('(')
    else:  # ')'
        stack.pop()
        if data[i-1] == '(':   # 바로 앞이 '('면 레이저
            answer += len(stack) #현재 스택에 있는 수 만큼 한번에 잘렸음
        else:                  # 쇠막대기 끝
            answer += 1 #쇠막대기 끝났으니까 하나 더해 

print(answer)
