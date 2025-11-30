# dp
# dp[1] = 1
# dp[2] = 2
# dp[3] = 4 .. 1+1+1 1+2 2+1 3
# dp[4] = 7 .. 1+1+1+1 1+1+2 2+1+1 3+1 3+1
#바텀업 방식이다

t = int(input())
for test_case in range(t):
    n = int(input())

    dp = [0] * (n+1)

    for i in range(1,n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] +dp[i-2]+dp[i-3]

    print(dp[n])