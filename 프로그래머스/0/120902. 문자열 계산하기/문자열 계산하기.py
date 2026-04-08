def solution(my_string):
    answer = 0
    
    my_string = list(my_string.split(" "))
    answer+=int(my_string[0])
    for i in range(len(my_string)-1):
        if my_string[i] == "+":
            answer+= int(my_string[i+1])
        elif my_string[i] == "-":
            answer-= int(my_string[i+1])
             
    return answer