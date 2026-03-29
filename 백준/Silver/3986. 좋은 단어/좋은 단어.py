n = int(input())
answer = 0
for _ in range(n):
    data = list(map(str, input().strip()))
    # print(data)
    stack = []
    for d in data:
        # print(d)
        if not stack:
            # print("emtpy append")
            stack.append(d)
        elif stack[-1] == d:
            # print("equal")
            stack.pop()
        else:
            # print("no")
            stack.append(d)
    # print(stack)
    if not stack:
        answer += 1

print(answer)