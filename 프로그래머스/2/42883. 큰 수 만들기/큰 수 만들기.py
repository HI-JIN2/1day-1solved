def solution(number, k):
    stack = []

    for n in number:
        # 앞에 숫자가 있고
        # 아직 지울 수 있고
        # 앞 숫자가 지금 숫자보다 작으면
        while True:
            if not stack:
                break

            if k <= 0:
                break

            if stack[-1] >= n:
                break

            stack.pop()
            k -= 1

        stack.append(n)

    # 아직 덜 지웠으면 뒤에서 제거
    while k > 0:
        stack.pop()
        k -= 1

    return ''.join(stack)