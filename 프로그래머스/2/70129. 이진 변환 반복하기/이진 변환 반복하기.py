def solution(s):
    answer = []
    l = list(s)
    
    result = 0
    zero_cnt = 0
    
    
    while True:
        cnt = l.count("1")
        zero_cnt += len(l)-cnt
        # print(bin(cnt)[2:])
        if bin(cnt)[2:] == "1":
            return [result+1,zero_cnt]
        else:
            result+=1
            l = bin(cnt)[2:]
            
    return answer