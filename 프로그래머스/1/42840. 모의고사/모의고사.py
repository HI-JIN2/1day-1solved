def solution(answers):
    result = []
    
    patterns = [
    [1,2,3,4,5],
    [2,1,2,3,2,4,2,5],
    [3,3,1,1,2,2,4,4,5,5]]
    
    score = [0]*3
    for i, answer in enumerate(answers):
        for j,pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                score[j] +=1
            
        
    m = max(score)

    for i,score in enumerate(score):
        if score== m:
            result.append(i+1)
    
    return result

