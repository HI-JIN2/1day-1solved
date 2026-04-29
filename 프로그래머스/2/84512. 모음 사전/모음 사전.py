from itertools import product

def solution(word):
    answer = 0
    words = [ "A", "E", "I","O","U", " "]
    result = []
    for c in product(words,repeat= 5):
        result.append("".join(c).replace(" ",""))
        
    result = sorted(set(result))
    # print(result)
    # result.index(word)
    

    return result.index(word)