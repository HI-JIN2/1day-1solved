#부녀회장
# a0b호에 살려면 아래층 1~b호 합친사람들을 데려와 살아야한다
#k0n호는 몇명이 사는지?


# 103호 001 002 003 => 1.2.3
# 101 102 103 => 1 3 6


# 203호
# 201 202 203 1 4 10

t=int(input())
for test_case in range(t):
    k = int(input())
    n = int(input())
    answer = 0

    dp = []
    for i in range(1,n+1):
        dp.append(i)
    # print(dp)

    for i in range(1,k+1): #0층~ k층
        for j in range(1,n): #1층~
            # print(j,dp[j],dp[j-1])
            dp[j] += dp[j-1]
        # print(dp)

    print(dp[n-1])

