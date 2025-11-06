t = int(input())
for _ in range(t):
    n , m = map(int,input().split())
    array = list(map(int,input().split()))

    d = [0] * (m+1)
    d[0] = 0
    for i in range(0, m-1):
        print(array[i*4:i*4+4])

        # for j in array[i:i+4]:
        d[i+1] = max(array[i*4:i*4+4])
        print(i, d)


    print(sum(d))

# 1
# 3 4
# 1 3 3 2 1 4 1 0 6 4 7