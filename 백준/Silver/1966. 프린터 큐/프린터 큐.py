#우선순위가 높다는걸 어캐 알지, max?

from collections import deque

t = int(input())
for _ in range(t):
    answer = []
    n,m=map(int,input().split()) #문서의 개수, 궁금한 문서의 현재 순서
    l = list(map(int,input().split()))

    dq = deque()
    for i,p in enumerate(l):
        dq.append((i,p))


    while dq:
        i, p = dq.popleft()
        # print(i,p)

        # 우선순위가 높다는걸 어캐 알지, max?
        if p == max(l):
            answer.append(i) #저장하는건 인덱스
            l.remove(p)
            # print("max")
        else:
            dq.append((i, p)) #최대 아니면 다시 넣어
            # print("no")
    # print(answer)
    print(answer.index(m)+1)
