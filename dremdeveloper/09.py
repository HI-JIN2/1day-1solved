# 10진수를 2진수로 변환
def solution(n):
    stack = []
    while n:
        stack.append(str(n % 2))
        n = n //2

    stack.reverse()
    return "".join(stack)


print(solution(10))
print(solution(13))
print(solution(27))
print(solution(12345))