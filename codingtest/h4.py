def count_signs(h, s, t):
    # 표지판 설치 횟수
    counts = {height: 0 for height in s}

    for x, d in t:
        low = x - d
        high = x
        for height in s:
            if low < height <= high:
                counts[height] += 1

    total = sum(counts.values())
    return counts, total


# 예시 입력
h = 10
s = [8, 2, 10]
t = [
    [1, 2], [2, 3], [3, 5], [3, 5],
    [1, 4], [6, 6], [2, 4], [8, 4],
    [12, 7], [12, 7], [1, 3]
]

counts, total = count_signs(h, s, t)
print(counts)  # {8: 3, 2: 6, 10: 1}
print(total)   # 10
