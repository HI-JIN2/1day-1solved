from itertools import permutations
def solution(numbers):
    answer = 0
    
    
    def is_prime(n):
        if n < 2:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True
    
    
    
    # 숫자 조합을 만들어냄
    # isprime 검사
    nums = []

    for l in range(1, len(numbers) + 1):
        for p in permutations(numbers, l):
            num = int(''.join(p))
            nums.append(num)
    nums = list(set(nums))
    for n in nums:
        if is_prime(n):
            answer+=1
    
    return answer