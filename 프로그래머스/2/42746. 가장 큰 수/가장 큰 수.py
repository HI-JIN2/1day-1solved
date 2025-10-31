def solution(numbers):
    numbers = list(map(str,numbers)) #문자로 바꿔줌
    
    numbers.sort(key = lambda x: x*3, reverse = True) #문자열인 상태에서 3개연속으로 붙이도록 
    

    return str(int(''.join(numbers)))
 