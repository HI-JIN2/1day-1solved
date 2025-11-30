n = int(input())
slist = []
dp =[0] * (n) #dp 리스트: 각 계단 단계별 최대값

for i in range(n):
    s = int(input())
    slist.append(s)


if n<=2:
    print(sum(slist))
else:
    dp[0] = slist[0]
    dp[1] = slist[0]+slist[1]
    for i in range(2,n):
        dp[i] = max(dp[i-3]+slist[i-1]+slist[i], dp[i-2]+slist[i] )

    print(dp[-1])
