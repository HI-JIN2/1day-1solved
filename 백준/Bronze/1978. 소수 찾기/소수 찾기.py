def is_prime_number(x):
    if x == 1:
        return False
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수 아님
    return True

N=int(input())
numbers=list(map(int, input().split()))

cnt=0
for i in numbers:
    
    if is_prime_number(i)==True:
        cnt+=1

print(cnt)        