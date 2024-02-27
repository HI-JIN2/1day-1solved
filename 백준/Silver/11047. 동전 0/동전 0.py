n , k = map(int,input().split())

coins = []
for i in range(n):
  coin = int(input())
  coins.append(coin)

coins.reverse()

ans = 0
for coin in coins:
  while k >= coin:
    ans = ans + (k//coin) #횟수
    k = k%coin
    if k<=0:
      break

print(ans)
  