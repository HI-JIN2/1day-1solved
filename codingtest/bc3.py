def min_chefs_needed(cooking_times, orders):
    """
    요리사의 최소 필요 인원을 계산하는 함수

    Args:
        cooking_times: 각 요리의 조리 시간 배열 (인덱스가 메뉴번호-1)
        orders: [데드라인, 메뉴번호] 형태의 주문 배열

    Returns:
        필요한 최소 요리사 수
    """
    # 각 주문의 (데드라인, 조리시간, 메뉴번호) 계산
    tasks = []
    for deadline, menu_num in orders:
        cooking_time = cooking_times[menu_num - 1]  # 메뉴번호는 1부터 시작
        tasks.append((deadline, cooking_time, menu_num))

    # 데드라인 순으로 정렬 (빠른 데드라인부터 처리)
    tasks.sort()

    # 각 요리사의 현재 작업 완료 시간을 추적
    chefs = []

    for deadline, cooking_time, menu_num in tasks:
        # 이 작업을 할당할 수 있는 요리사 찾기
        # (현재 시점에서 작업을 시작해도 데드라인에 맞출 수 있는 요리사)
        best_chef = -1
        earliest_finish = float('inf')

        for i, chef_busy_until in enumerate(chefs):
            # 이 요리사가 현재 작업을 끝내고 새 작업을 시작할 수 있는 시간
            start_time = chef_busy_until
            # 새 작업 완료 시간
            finish_time = start_time + cooking_time

            # 데드라인을 맞출 수 있고, 가장 일찍 끝낼 수 있는 요리사 선택
            if finish_time <= deadline and finish_time < earliest_finish:
                best_chef = i
                earliest_finish = finish_time

        if best_chef != -1:
            # 기존 요리사에게 할당
            chefs[best_chef] = earliest_finish
        else:
            # 새로운 요리사가 필요
            # 새 요리사는 시간 0부터 시작 가능
            new_finish_time = cooking_time
            if new_finish_time <= deadline:
                chefs.append(new_finish_time)
            else:
                # 이론적으로 불가능한 경우 (데드라인이 조리시간보다 짧음)
                return -1  # 에러 표시

    return len(chefs)


# 테스트 케이스 1
cooking_times1 = [30, 60, 120]
orders1 = [[90, 2], [120, 1], [120, 3], [135, 1], [135, 1], [180, 3]]
result1 = min_chefs_needed(cooking_times1, orders1)
print(f"테스트 1 결과: {result1}")  # 예상: 2

# 테스트 케이스 2
cooking_times2 = [3, 5, 6]
orders2 = [[4, 1], [10, 3], [20, 2], [14, 3]]
result2 = min_chefs_needed(cooking_times2, orders2)
print(f"테스트 2 결과: {result2}")  # 예상: 1


# 디버깅을 위한 상세 정보 출력 함수
def debug_chef_schedule(cooking_times, orders):
    """스케줄링 과정을 상세히 출력하는 디버깅 함수"""
    print(f"조리시간: {cooking_times}")
    print(f"주문 (데드라인, 메뉴): {orders}")

    tasks = []
    for deadline, menu_num in orders:
        cooking_time = cooking_times[menu_num - 1]
        tasks.append((deadline, cooking_time, menu_num))

    tasks.sort()
    print(f"작업 스케줄 (데드라인, 조리시간, 메뉴): {tasks}")

    chefs = []
    print("\n스케줄링 과정:")

    for deadline, cooking_time, menu_num in tasks:
        best_chef = -1
        earliest_finish = float('inf')

        for i, chef_busy_until in enumerate(chefs):
            start_time = chef_busy_until
            finish_time = start_time + cooking_time

            if finish_time <= deadline and finish_time < earliest_finish:
                best_chef = i
                earliest_finish = finish_time

        if best_chef != -1:
            old_finish = chefs[best_chef]
            chefs[best_chef] = earliest_finish
            print(f"메뉴{menu_num} (조리{cooking_time}분, 데드라인{deadline}분): 요리사 {best_chef + 1}에게 할당")
            print(f"  {old_finish}분부터 시작 → {earliest_finish}분 완료")
        else:
            new_finish_time = cooking_time
            if new_finish_time <= deadline:
                chefs.append(new_finish_time)
                print(f"메뉴{menu_num} (조리{cooking_time}분, 데드라인{deadline}분): 새 요리사 {len(chefs)}에게 할당")
                print(f"  0분부터 시작 → {new_finish_time}분 완료")
            else:
                print(f"메뉴{menu_num}: 불가능! (조리시간 {cooking_time} > 데드라인 {deadline})")
                return -1

        print(f"  현재 요리사들의 작업완료시간: {chefs}")

    print(f"\n필요한 요리사 수: {len(chefs)}")
    return len(chefs)


print("\n=== 디버깅 정보 ===")
print("테스트 케이스 1:")
debug_chef_schedule(cooking_times1, orders1)

print("\n테스트 케이스 2:")
debug_chef_schedule(cooking_times2, orders2)