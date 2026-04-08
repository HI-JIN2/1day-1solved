def solution(hp):
    
    high = hp//5
    mid = hp%5//3
    low = hp%5%3
    
    return high+mid+low