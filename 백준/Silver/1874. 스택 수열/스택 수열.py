n = int(input())
target = [int(input()) for _ in range(n)]

stack = []
answer = []
cur = 1

for num in target:
    # 필요한 숫자까지 push
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1

    # top이 같으면 pop
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        exit()

print("\n".join(answer))