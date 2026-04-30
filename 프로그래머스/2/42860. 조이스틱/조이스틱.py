def solution(name):
    answer = 0
    n = len(name)

    move = n - 1  # 오른쪽으로 쭉 가는 기본 이동

    for i in range(n):
        # 1. 알파벳 위/아래 조작
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)

        # 2. i 뒤의 연속 A 구간 찾기
        next = i + 1
        while next < n and name[next] == 'A':
            next += 1

        # 3. 커서 이동 최솟값 갱신
        move = min(
            move,
            2 * i + n - next,        # 오른쪽 갔다가 왼쪽으로 돌아가기
            i + 2 * (n - next)       # 왼쪽 갔다가 오른쪽으로 돌아오기
        )
    # print(answer,move)
    return answer + move