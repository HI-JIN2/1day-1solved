# 좋아요 — 이 문제는 **“시뮬레이션 + 구현”** 유형이면서, **호텔 객실 예약 시스템 / 구간 관리 문제**로 볼 수 있습니다.
# 정확히는 **“2차원 배열(층 × 객실)을 날짜별로 상태 갱신하며 시뮬레이션하는 구현 문제”** 입니다.
# 또한 예약의 시작/종료일에 따라 객실 상태를 관리해야 하므로, **interval scheduling (구간 스케줄링)** 문제의 변형으로 분류할 수도 있습니다.
#
# ---
# 
# ## 🔍 문제 요약
#
# * 호텔은 `h`층, 층마다 `w`개의 객실이 있다.
# * 각 예약 `[rooms, check_in, check_out]`은 **같은 층의 연속된 rooms개 객실**을 원한다.
# * 예약은 **가장 아래층부터 가능한 층에 배정**한다.
# * 예약 기간 동안은 해당 객실이 점유된다.
# * 예약이 가능하면 1, 불가능하면 0을 결과 리스트에 담는다.
#
# ---
#
# ## 🧠 접근 아이디어
#
# 1. 날짜별 객실 점유 상태를 관리한다.
#
#    * `hotel[floor][room]`에 각 날짜별 예약 여부를 기록.
#    * Python에서는 `defaultdict(set)` 형태로 `(층, 객실)`의 예약일을 저장하거나
#      `hotel[floor][room] = list of (start, end)`로 저장 가능.
# 2. 각 예약마다 1층부터 확인해서:
#
#    * 그 층에 **연속된 rooms개 객실이 모두 비어 있는지**를 체크.
#    * 가능하면 그 구간을 예약(occupied) 표시.
#    * 없으면 다음 층으로 넘어감.
# 3. 끝까지 없으면 예약 불가능(0).
#
# ---
#
# ## ✅ 코드 구현 (Python)
#
# ```python
# def hotel_booking(h, w, books):
#     # 각 층마다 객실별로 예약된 (start, end) 구간을 저장
#     hotel = [[[] for _ in range(w)] for _ in range(h)]
#     result = []
#
#     for rooms, start, end in books:
#         booked = False  # 이번 예약이 가능한지 여부
#
#         for floor in range(h):  # 아래층부터 탐색
#             # 가능한 연속된 객실 찾기
#             for i in range(w - rooms + 1):
#                 segment = list(range(i, i + rooms))
#                 # 이 segment의 객실들이 기간(start, end) 동안 비어있는지 체크
#                 can_book = True
#                 for room in segment:
#                     for (s, e) in hotel[floor][room]:
#                         # 겹치는 구간이 하나라도 있으면 불가
#                         if not (end <= s or e <= start):
#                             can_book = False
#                             break
#                     if not can_book:
#                         break
#                 if can_book:
#                     # 예약 등록
#                     for room in segment:
#                         hotel[floor][room].append((start, end))
#                     booked = True
#                     break  # 더 이상 탐색 X
#             if booked:
#                 break
#
#         result.append(1 if booked else 0)
#
#     return result
#
#
# # 예시 실행
# h, w = 2, 4
# books = [[3,1,3],[2,1,4],[1,1,2],[1,1,5],[2,2,5],[2,3,5]]
# print(hotel_booking(h, w, books))  # [1, 1, 1, 1, 0, 1]
# ```
#
# ---
#
# ## 🧩 설명
#
# 1. **[3,1,3]** → 1층에 3개 연속 가능 → ✅
# 2. **[2,1,4]** → 1층 남은 자리 부족 → 2층에 가능 → ✅
# 3. **[1,1,2]** → 1층 남은 한 자리 → ✅
# 4. **[1,1,5]** → 2층 남은 자리 가능 → ✅
# 5. **[2,2,5]** → 1,2층 모두 연속된 2칸 없음 → ❌
# 6. **[2,3,5]** → 3일 시점에 1층 비었음 → ✅
#    결과 `[1, 1, 1, 1, 0, 1]`
#
# ---
#
# ## 📚 유형 정리
#
# | 분류    | 세부 유형               | 설명                                    |
# | ----- | ------------------- | ------------------------------------- |
# | 시뮬레이션 | 호텔 객실 배정 시뮬레이션      | 날짜·층·객실 상태를 갱신하며 처리                   |
# | 구현    | 2중/3중 루프 구조         | 층, 객실, 날짜별 상태 확인                      |
# | 구간 관리 | Interval Scheduling | 구간 겹침 여부(`end <= s or e <= start`) 판단 |
#
# ---
#
# 원한다면 이걸 **시간 복잡도 O(h * w * N)**에서
# 더 효율적으로 (예: 누적합, 세그먼트 트리, 우선순위 큐로 층별 가용성 관리) 개선하는 버전도 보여드릴 수 있습니다.
# 그럴까요?



def hotel_booking(h, w, books):
    # 각 층마다 객실별로 예약된 (start, end) 구간을 저장
    hotel = [[[] for _ in range(w)] for _ in range(h)]
    result = []

    for rooms, start, end in books:
        booked = False  # 이번 예약이 가능한지 여부

        for floor in range(h):  # 아래층부터 탐색
            # 가능한 연속된 객실 찾기
            for i in range(w - rooms + 1):
                segment = list(range(i, i + rooms))
                # 이 segment의 객실들이 기간(start, end) 동안 비어있는지 체크
                can_book = True
                for room in segment:
                    for (s, e) in hotel[floor][room]:
                        # 겹치는 구간이 하나라도 있으면 불가
                        if not (end <= s or e <= start):
                            can_book = False
                            break
                    if not can_book:
                        break
                if can_book:
                    # 예약 등록
                    for room in segment:
                        hotel[floor][room].append((start, end))
                    booked = True
                    break  # 더 이상 탐색 X
            if booked:
                break

        result.append(1 if booked else 0)

    return result


# 예시 실행
h, w = 2, 4
books = [[3,1,3],[2,1,4],[1,1,2],[1,1,5],[2,2,5],[2,3,5]]
print(hotel_booking(h, w, books))  # [1, 1, 1, 1, 0, 1]


h, w = 1,100
books = [[100,1,10],[100,1,2],[1,2,3],[1,3,4]]
print(hotel_booking(h, w, books))  # [1, 0,0,0]

h, w = 1,100
books = [[100,1,2],[100,1,10],[1,2,3],[1,3,4]]
print(hotel_booking(h, w, books))  # [1, 0, 1,1]

