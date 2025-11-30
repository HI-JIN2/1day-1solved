# dp
# dp[1]=1
# dp[2]= 2
# dp[3] = 3
# dp[4]= 5
# dp [9] = 55

n = int(input())
dp = [0]*(n+1)

for i in range(1,n+1):
    if i == 1 :
        dp[i] = 1
    elif i ==2:
        dp[i] = 2
    else:
        dp[i] =(dp[i-1] + dp[i-2])%10007 #

print(dp[n])