def solution(arr):
    
    answer =[]
    j=arr[0]
    start=arr[0]
    for i in arr:
        if i ==j:
            j=i
        else:
            answer.append(i)
            j=i

    answer.insert(0,start)
    return answer