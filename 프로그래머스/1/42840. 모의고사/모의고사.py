def solution(answers):
    answer = []
    
    patterns = [
    [1,2,3,4,5],
    [2,1,2,3,2,4,2,5],
    [3,3,1,1,2,2,4,4,5,5]]
    
    score = [0]*3

    for i,a in enumerate(answers):
        for j in range(3):
            if a == patterns[j][i%len(patterns[j])]:
                score[j] +=1
    
    # print(score)
    max_score = max(score)
    for i, s in enumerate(score):
        if max_score == s:
            answer.append(i+1)
            

    return answer

