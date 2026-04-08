def solution(routes): 
    answer = 1 
    routes = sorted(routes, key = lambda x: (x[1], x[0])) 
    # print(routes) 
    cam = routes[0][1] #첫번째 차의 진출점 
    for start, end in routes: 
        if start <= cam <= end: 
            continue #찍혔음 
        else: answer +=1 
        cam = end 
        
    return answer