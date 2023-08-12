arr = []
arr_size = []


for _ in range(5):
    j = input()
    arr.append(j)
    arr_size.append(len(j))

result=""

for i in range(max(arr_size)):
    for j in range(5):
        if i <arr_size[j]:
            result+=arr[j][i]

print(result)