n, x = map(int, input().split())
l = list(map(int, input().split()))

if max(l) == 0:
    print('SAD')
    exit(0)

value = sum(l[:x]) 
max_value = value
max_cnt = 1

for i in range(x, n):
    value += l[i] 
    value -= l[i-x] 

    if value > max_value: #max값 갱신
        max_value = value
        max_cnt = 1 
    elif value == max_value: #max값이 같은 날을 세야함
        max_cnt += 1

print(max_value)
print(max_cnt)
