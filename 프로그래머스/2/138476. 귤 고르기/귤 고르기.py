from collections import defaultdict
def solution(k, tangerine):
    d = defaultdict(int)
    for i in tangerine:
        d[i]+=1
            
    d = sorted(d.items(), key = lambda x: -x[1])
    
    result = []
    for key, c in d:
        for _ in range(c): #개수
            if len(result)<k:
                result.append(key)
    
    # print(len(set(result)))
    return len(set(result))