def solution(N, stages):
    num = []
    per = []

    for i in range(1, N + 1):
        num.append(stages.count(i))

    t = len(stages)
    cnt = 0
    for i in num:
        if i == 0:
            per.append(i)
        else:
            per.append(i / (t - cnt))
        cnt += i

    sorted_indexed_list = sorted(enumerate(per), key=lambda x: x[1], reverse=True)

    # 정렬된 결과에서 인덱스만 추출
    sorted_indices = [index + 1 for index, value in sorted_indexed_list]
    # print(sorted_indices)

    return sorted_indices

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))