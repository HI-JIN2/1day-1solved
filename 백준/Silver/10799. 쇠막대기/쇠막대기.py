data = input()
stack = []
answer = 0

for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
    else:  # ')'
        stack.pop()
        if data[i-1] == '(':   # 바로 앞이 '('면 레이저
            answer += len(stack)
        else:                  # 쇠막대기 끝
            answer += 1

print(answer)