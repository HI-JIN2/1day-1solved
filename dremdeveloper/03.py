# 두개 뽑아서 더하기

# def solution(arr):
#     new = []
#     arr2 = arr[1:-1]
#     for i in arr:
#         for j in arr2:
#             new.append(i+j)
#     new = list(set(new))
#     return new

def solution(arr):
    new = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j :
                continue
            else:
                new.append(arr[i]+arr[j])
    new = sorted(list(set(new))) #sorted가 list로 반환하기에 list는 없어도 되긴함.
    # 왜인지 모르겠으나 테케 2개가 통과가 안되기 떄문에 sorted 추가하면 됨
    return new

l= [2,1,3,4,1,9,1]
# l = [5,0,2,7]
print(solution(l))