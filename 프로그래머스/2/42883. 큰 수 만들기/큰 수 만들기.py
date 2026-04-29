def solution(number, k):
    stack = []

    for n in number:
        while stack and k > 0 and stack[-1] < n: #현재값이 마지막값 보다 클때 막값 지워. 큰값인 내가 더 앞으로가야 유리하기 때문
            stack.pop()
            k -= 1

        stack.append(n)

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)
