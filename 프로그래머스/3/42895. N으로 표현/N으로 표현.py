def solution(N, number):
    
    memo = []
    for i in range(1,9):
        numbers ={int(str(N)*i)}
        for j in range(i-1):
            for x in memo[j]:
                for y in memo[-j-1]:
                    numbers.update([x+y, x-y, x*y])
                    if y != 0:
                        numbers.add(x//y)
                        
        if number in numbers:
            return i
        
        memo.append(numbers)
    
    return -1