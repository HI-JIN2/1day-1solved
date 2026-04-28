from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    album = defaultdict(list)
    total = defaultdict(int)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        album[g].append((p,i))
        total[g]+=p
    
    arr = sorted(total.items(), key = lambda x: -x[1])
    # print(arr)
    
    
    for a in arr:
        num = sorted(album[a[0]], key = lambda x: -x[0])
        # print(num)
        answer.append(num[0][1])
        if len(num)>=2:        
            answer.append(num[1][1])
    
    return answer