# 리스트에 있는 두 개의 수로 특정값 만들기

def solution(arr,target):
    hash = [0]  *(target+1)
    for i in arr:
        if i <=target:
            hash[i] = 1 #0을 1로 바꿈

    # arr = list(set(arr))

    for i in arr:
        if i >=target: #타겟보다 더 큰수는 답이 될 수 없음
            continue

        if (target -i) ==i : # arr에 중복되는 원소는 존재하지 않음
            # 5+5=10이 될 수 없다는 말임
            # 6+6=12도 마찬가지
            continue

        if (hash[target-i]):
            # 6-1 =5 hash[5]가 1이면 true x
            #6-2=4 hash[4]가 1이면 true o
            return True

    return False

print(solution([1,2,3,4,8],6))
print(solution([2,3,5,9],10))