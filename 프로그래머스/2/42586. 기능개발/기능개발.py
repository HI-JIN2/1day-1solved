import math

def solution(progresses, speeds):
    answer = []
    days = [ math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    # print(days)
    
    max_day = days[0]
    feat_cnt=0
    for d in days:
        # print(d)
        if max_day>=d:
            # print(max_day,d)
            feat_cnt+=1
        else:
            # print(max_day,d)
            answer.append(feat_cnt) #이전거 
            feat_cnt=1
            max_day = d
    answer.append(feat_cnt)

    return answer