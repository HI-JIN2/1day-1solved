def solution(score):
    answer = [0]*len(score)
    
    avg_score = [] #평균 점수
    
    for i, s in enumerate(score):
        avg_score.append((i+1, (s[0]+s[1])/2))
    avg_score = sorted(avg_score, key = lambda x: x[1], reverse = True) #점수를 기준으로 내림차순 정렬
    # print(avg_score)
    
    before_score = 0 
    price = 0 #등수
    same_price_cnt = 0 #동점자 수 
    
    for num, socre in avg_score: 
        if before_score == socre: #전 사람이랑 점수가 같으면
            answer[num-1] = price
            same_price_cnt +=1
        else:
            price+= (1+same_price_cnt)
            answer[num-1] = price
            before_score = socre
            same_price_cnt = 0
            
        # print(n,s)
    
    return answer