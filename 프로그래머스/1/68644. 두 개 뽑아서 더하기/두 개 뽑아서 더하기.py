def solution(arr):
    new = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if i == j :
                continue
            else:
                new.append(arr[i]+arr[j])
    new = sorted(list(set(new)))
    return new