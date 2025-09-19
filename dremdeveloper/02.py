# def solution(arr):
#     a =set(arr) #중복값 제어
#     a= list(a)
#     a.sort(reverse=True) #내림차순
#     return a

def solution(arr):
    a = list(set(arr))
    a.sort(reverse = True)
    return a


l = [2,1,1,3,2,5,4]
print(solution(l))