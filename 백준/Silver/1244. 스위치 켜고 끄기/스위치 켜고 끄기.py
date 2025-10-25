n = int(input())
switch = list(map(int, input().split()))
student_cnt = int(input())

for _ in range(student_cnt):
    gender, num = map(int, input().split())

    if gender == 1:  # 남학생
        for i in range(num - 1, n, num):
            switch[i] = 1 - switch[i]
    else:  # 여학생
        num -= 1  # 인덱스 보정
        left = right = num
        while left - 1 >= 0 and right + 1 < n and switch[left - 1] == switch[right + 1]:
            left -= 1
            right += 1
        for i in range(left, right + 1):
            switch[i] = 1 - switch[i]

for i in range(n):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
