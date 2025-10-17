# import time
#
# def solution(message, spoiler_ranges):
#     start_time = time.perf_counter() # 코드 시작 시간 기록
#     n = len(message)
#     m = len(spoiler_ranges)
#
#     # 1) 각 인덱스가 몇 번째 스포 구간에 속하는지 기록 (-1: 일반 구간)
#     #    구간들은 겹치지 않고 start 오름차순으로 주어진다고 했으므로 한 칸엔 최대 1개 구간만 해당
#     belong = [-1] * n
#     for idx, (s, e) in enumerate(spoiler_ranges):
#         # 문제는 [start, end] 양끝 **모두 포함** 구간
#         for i in range(s, e + 1):
#             belong[i] = idx
#
#     # 2) 단어 구간(시작, 끝), 단어 문자열을 모두 추출
#     words = []  # (start, end, text)
#     i = 0
#     while i < n:
#         if message[i].isalnum() and message[i].islower() or message[i].isdigit():
#             # 위 조건은 소문자/숫자 판별인데, 단순화를 위해 isalnum + 소문자/숫자 조합으로 처리
#             # 실제로는 메시지가 소문자/숫자/공백으로만 주어진다고 했으니 아래처럼 더 안전하게:
#             if message[i].isdigit() or ('a' <= message[i] <= 'z'):
#                 j = i
#                 while j < n and (message[j].isdigit() or ('a' <= message[j] <= 'z')):
#                     j += 1
#                 words.append((i, j - 1, message[i:j]))
#                 i = j
#                 continue
#         i += 1
#
#     # 3) 어떤 단어가 "스포가 아닌 구역에서"라도 등장하면 중요 단어 자격 박탈
#     has_clean_occurrence = set()
#     for s, e, w in words:
#         # s..e 중 스포 구간에 속하는 인덱스가 하나도 없으면 "깨끗한(스포 아님) 등장"
#         clean = True
#         k = s
#         while k <= e:
#             if belong[k] != -1:
#                 clean = False
#                 break
#             k += 1
#         if clean:
#             has_clean_occurrence.add(w)
#
#     # 4) 각 스포 단어가 "언제 완전히 공개되는지(=걸친 스포 구간 중 가장 늦게 클릭되는 구간 index)"
#     #    를 계산해 시점별로 묶기
#     by_time = [[] for _ in range(m)]  # time -> list of (start_pos, word)
#     for s, e, w in words:
#         latest = -1
#         k = s
#         while k <= e:
#             if belong[k] != -1:
#                 if belong[k] > latest:
#                     latest = belong[k]
#             k += 1
#         if latest != -1:  # 스포 단어일 때만
#             by_time[latest].append((s, w))
#
#     # 5) 클릭을 왼쪽→오른쪽 시점으로 진행하며, 같은 시점에 공개되는 단어들은
#     #    시작 위치 기준으로 정렬(왼쪽부터 판단)
#     seen_important = set()
#     answer = 0
#
#     for t in range(m):
#         if not by_time[t]:
#             continue
#         by_time[t].sort(key=lambda x: x[0])  # 왼→오 순서
#         for _, w in by_time[t]:
#             if w in has_clean_occurrence:
#                 continue          # 조건 2 위반
#             if w in seen_important:
#                 continue          # 조건 3 위반(중복)
#             # 조건 1은 이미 스포 단어라서 충족
#             seen_important.add(w)
#             answer += 1
#
#     end_time = time.perf_counter()  # 코드 종료 시간 기록
#
#     elapsed_time = end_time - start_time  # 경과 시간 계산
#     print(f"실행 시간: {elapsed_time:.4f} 초")  # 소수점 4자리까지 출력
#     return answer


def solution(message, spoiler_ranges):
    n = len(message)
    m = len(spoiler_ranges)

    # 1) 각 인덱스가 어떤 스포 구간에 속하는지 기록 (-1 = 스포 아님)
    belong = [-1] * n
    for idx, (s, e) in enumerate(spoiler_ranges):
        for i in range(s, e + 1):  # 포함 구간
            belong[i] = idx

    # 2) 단어 추출
    words = []  # (start, end, word)
    i = 0
    while i < n:
        ch = message[i]
        print(ch)
        if ch.isdigit() or ('a' <= ch <= 'z'):
            j = i + 1
            while j < n and (message[j].isdigit() or ('a' <= message[j] <= 'z')):
                j += 1
            words.append((i, j - 1, message[i:j]))
            i = j
        else:
            i += 1
    print(words)

    # 3) 단어별로 걸친 스포 구간의 최대 index (latest) 계산
    has_clean_occurrence = set()
    by_time = [[] for _ in range(m)]  # idx 시점 -> [(start, word)]

    for s, e, w in words:
        latest = -1
        k = s
        while k <= e:
            if belong[k] != -1:  # 스포에 속하면
                latest = max(latest, belong[k])
            k += 1

        if latest == -1:
            has_clean_occurrence.add(w)   # 스포 전혀 안 걸침
        else:
            by_time[latest].append((s, w))  # 이 시점에 완전 공개

    # 4) 공개 시점 순서대로 처리
    seen_important = set()
    answer = 0
    for t in range(m):
        print(t, by_time[t])
        if not by_time[t]:
            continue
        by_time[t].sort(key=lambda x: x[0])  # 왼→오
        for _, w in by_time[t]:
            if w in has_clean_occurrence:
                continue
            if w in seen_important:
                continue
            seen_important.add(w)
            answer += 1

    return answer

print(solution("here is muzi here is a secret message", [[0, 3], [23, 28]]))
print(solution("my phone number is 01012345678 and may i have your phone number", [[5, 5], [25, 28], [34, 40], [53, 59]]))