def solution(lottos, win_nums):
    
    print(lottos)
    
    cnt=0
    z=0
    for i in lottos:
        if i in win_nums:
            print(i,"있다")
            cnt+=1
        elif i ==0:
            print("0추가요")
            z+=1
        else :
            print(i,"이건 없어")
    
    
    answer = []
    
    print(cnt,z)
    result = 7-cnt
    if(result>6):
        result =6
    rresult = result-z

    if (z==6):
        rresult =1
        result =6
        
    # rresult = result-z
    
    answer.append(rresult)
    answer.append(result)
    return answer