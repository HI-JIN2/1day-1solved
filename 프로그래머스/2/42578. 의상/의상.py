from collections import defaultdict
def solution(clothes):
    answer = 1
    
    arr = defaultdict(int)
    for name, c_type in clothes:
        arr[c_type]+=1
        
    # print(arr)
    for i in arr.values():
        answer*=(i+1)
    return answer-1