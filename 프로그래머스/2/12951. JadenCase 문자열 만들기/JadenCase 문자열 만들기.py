def solution(s):
    answer = []
    
    arr = list(map(str,s.split(" ")))
    # print(arr)
    
    for a in arr:
        if a:
            if a[0].islower():
                # print(chr(ord(a[0]) - 32))
                word = chr(ord(a[0]) - 32)+a[1:].lower()
                answer.append(word)
            else:
                answer.append(a[0] + a[1:].lower())
        else:
            answer.append(a) 
    return " ".join(answer)
#즉 직접 " " 붙이고 [:-1] 하지 말고, split(" ") 결과를 변환한 뒤 다시 " ".join() 해야 해.