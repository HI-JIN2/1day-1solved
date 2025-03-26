def solution(price, money, count):
    answer = 0
    hap=0
    
    for i in range(count+1):
        print(hap,price*i)
        hap+= price*i
        
        # print(hap)
    answer = hap-money
    if answer<0:
        answer =0

    return answer