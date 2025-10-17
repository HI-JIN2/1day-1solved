def solution(dist_limit: int, split_limit: int) -> int:
    # 완전 분할 x회(2), y회(3) 후, 마지막 한 레벨을 부분 분할(2 또는 3)까지 고려
    if dist_limit <= 0 or split_limit < 2:
        return 1

    # 2^x, 3^y 미리
    p2 = [1]
    while p2[-1] <= split_limit // 2:
        p2.append(p2[-1] * 2)
    p3 = [1]
    while p3[-1] <= split_limit // 3:
        p3.append(p3[-1] * 3)

    best = 1

    # 완전 분할 비용(노드 수) 공식
    # C_min(x,y) = (2^x - 1) + 2^x * (3^y - 1) / 2
    def full_cost(x, y):
        if x == 0:
            return (p3[y] - 1) // 2
        return (p2[x - 1] * (p3[y] + 1)) - 1

    for x in range(len(p2)):              # 2를 x번 완전 분할
        for y in range(len(p3)):          # 그 다음 3을 y번 완전 분할
            P = p2[x] * p3[y]             # 완전 분할 후 리프 수(=분배도)
            if P > split_limit:
                break

            cost = full_cost(x, y)
            if cost > dist_limit:
                break

            # 완전 분할만 해도 되는 경우
            best = max(best, P)

            # 남은 예산으로 "한 레벨 부분 분할" 시도
            rem = dist_limit - cost
            if rem == 0:
                continue

            # 다음 레벨에서 분할 가능한 최대 리프 개수
            candidates = []

            # 부분 3-분할이 가능하면, 한 레벨에서 최대 min(rem, P)개를 3으로 분할
            if P * 3 <= split_limit:
                candidates.append(P + 2 * min(rem, P))

            # 부분 2-분할이 가능하면, 한 레벨에서 최대 min(rem, P)개를 2로 분할
            if P * 2 <= split_limit:
                candidates.append(P + 1 * min(rem, P))

            if candidates:
                best = max(best, max(candidates))

    return best

print(solution(3,6)) #6

print(solution(0,10)) #1
print(solution(3,100)) #7
print(solution(5,16)) #9


