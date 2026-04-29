def solution(s):
    answer = ""
    arr = list(map(int,s.split()))
    # print(arr)
    answer += str(min(arr))
    answer += " "
    answer += str(max(arr))
    # print(answer)
    
    
    return answer