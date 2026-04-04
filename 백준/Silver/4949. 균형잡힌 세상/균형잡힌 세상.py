

while True:

    data = input()
    if data == ".":
        exit()

    stack = [ ]
    l = list(data)
    for i in l:
        if i == "(":
            # print("hit", i)
            stack.append(i)
        elif i == "[":
            # print("hit",i)
            stack.append(i)
        elif i==")" :
            if stack and "(" == stack[-1]:
                 stack.pop()
            else:
                stack.append(i)
                break
        elif i=="]":
            if stack and "[" == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
                break
    # print(stack)
    if len(stack) == 0:
        print("yes")
    else:
        print("no")