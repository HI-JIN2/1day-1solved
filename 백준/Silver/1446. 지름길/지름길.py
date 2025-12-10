#그리디로 하면 정답 안나옴 dp로 해야함

n, dist = map(int, input().split())
glist = [[] for _ in range(dist + 1)]
dp = [i for i in range(dist + 1)]  # dp[i] = i까지의 최소거리

for _ in range(n):
    s, e, g = map(int, input().split())
    if e <= dist: #도착점보다 큰건 거름
        glist[s].append((e, g))


for i in range(dist + 1):
    if i > 0:
        dp[i] = min(dp[i], dp[i - 1] + 1) # 일반도로 1 이동

    for e, g in glist[i]:
        dp[e] = min(dp[e], dp[i] + g) # 지름길 적용

print(dp[dist])
