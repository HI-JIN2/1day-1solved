t = int(input())
for test_case in range(t):
    stack = []
    li = list(input())
    for l in li:
        # print(stack)
        if l == "(":
            stack.append(l)
        elif l == ")" and len(stack):
            # print(l)
            stack.pop()
        else:
            stack.append(l)
            break

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")