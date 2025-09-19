def solution(arr):
    arr.sort()
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


l = [1,-5,2,4,3]
result =  solution(l)
print(result)

print(bubble_sort(l))