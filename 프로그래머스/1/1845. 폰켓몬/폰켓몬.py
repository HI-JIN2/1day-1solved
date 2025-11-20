def solution(nums):
    cnt = len(nums)//2
    
    snumcnt = len(set(nums))
    if cnt<snumcnt:
        return cnt
    else: return snumcnt