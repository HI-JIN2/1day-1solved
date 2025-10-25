import math

n = int(input())
answer = n

# 2부터 n의 제곱근까지의 모든 수 확인
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        # n에서 i를 나눌 수 있는 만큼 나눠줌
        while n % i == 0:
            n //= i
        # 오일러 피 함수: (1 - 1/i)
        answer = answer * (1 - 1/i)

# 자기 자신이 소수임 
if n > 1:
    answer = answer * (1 - 1/n)

print(int(answer))
