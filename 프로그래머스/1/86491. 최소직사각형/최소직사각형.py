def solution(sizes):
    arr1 = []
    arr2 = []
    
    for x,y in sizes:
        if x>y:
            arr1.append(x)
            arr2.append(y)
        else:
            arr1.append(y)
            arr2.append(x)
   
    return  max(arr1) * max(arr2)