def solution(array, n):
    
    abs_list = []

    for a in array:
        abs_list.append((a,abs(n-a)))
    
    abs_list = sorted(abs_list, key= lambda x: (x[1], x[0]))
    # print(abs_list)
                        
    return abs_list[0][0]