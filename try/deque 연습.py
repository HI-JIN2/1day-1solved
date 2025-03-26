from collections import deque


dq = deque('love')
print(dq)

# 스택
dq.append('m')
print(dq)

dq.pop()
print(dq)

# 큐
dq.appendleft('l')
print(dq)

dq.pop()
print(dq)

dq.append('p')
print(dq)

dq.popleft()
print(dq)

#deque 확장하기
dq.extend('you')
print(dq)

dq.extendleft('l')
print(dq)

#리스트처럼 사용
dq[2]='n'
print(dq)

dq.insert(2,'p')
print(dq)

dq.remove('p')
print(dq)

# 반전
dq.reverse()
print(dq)
