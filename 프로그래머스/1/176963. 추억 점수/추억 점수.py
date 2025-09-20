def solution(name, yearning, photo):
    answer = []
    
    
    for i in photo:
        cnt =0
        for j in i:
            if j in name:
                # print("있다")
                y = yearning[name.index(j)]
                # print(y)
                cnt=cnt+y
        answer.append(cnt)
    
    return answer