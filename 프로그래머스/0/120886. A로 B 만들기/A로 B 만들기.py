def solution(before, after):
    answer = 0
    
    before = list(before)
    before.sort()
    
    after = list(after)
    after.sort()
    
    for (b, a) in zip(before, after):
        if b!=a:
            return 0
    return 1