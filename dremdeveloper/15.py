#요세푸스문제

from collections import deque

def solution(n,k):
    queue = deque()

    for i in range(n):
        queue.append(i+1)

    while len(queue) >1:
        for _ in range(k-1):
            a=queue.popleft()
            # print(a,"를 붙여요")
            queue.append(a)
        queue.popleft()
        # print(queue)

    return queue[0]

# a = deque()
# [a.append(i) for i in range(5)]
# print(a)
# a.pop()
# print(a)
#
# b = deque()
# [b.append(i) for i in range(5)]
# print(b)
# b.popleft()
# print(b)

print(solution(5,2))
print(solution(5,3))