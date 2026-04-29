from itertools import permutations

def solution(A,B):
    
    #순서가 있는 조합
    A = sorted(A)
    B = sorted(B, reverse= True)

    num = 0
    for i,j in zip(A,B):
        num += (i*j)
        
    return num