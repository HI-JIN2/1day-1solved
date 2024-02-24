def solution(array):
    cnt=0 
    for i in array:
        for j in str(i):
            if j == "7":
                cnt+=1
                
    return cnt