def solution(s):
    answer = ""
    
    l = ["zero", "one", "two", "three","four","five","six","seven", "eight", "nine"]

    # print(l)
    
    letter = ""
    for i in s:
        # print(i)
        if i.isalpha():
            letter += i
        else: 
            answer += i
            # print(l.index(letter))
            
        if letter != "" and letter in l:
            # print(letter)
            answer += str(l.index(letter))
            letter = ""
    return int(answer)