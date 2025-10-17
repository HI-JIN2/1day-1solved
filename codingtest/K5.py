def solution(board, commands):
    n, m = len(board), len(board[0])

    # 현재 보드에서 각 id의 직사각형 경계 수집
    def collect_rects(bd):
        rect = {}
        for r in range(n):
            for c in range(m):
                v = bd[r][c]
                if v == 0:
                    continue
                if v not in rect:
                    rect[v] = [r, c, r, c]
                else:
                    r1, c1, r2, c2 = rect[v]
                    rect[v] = [min(r1, r), min(c1, c), max(r2, r), max(c2, c)]
        return rect

    # 한 칸 이동 후의 목적지 직사각형
    def dest_rect(rc, d):
        r1, c1, r2, c2 = rc
        h, w = r2 - r1 + 1, c2 - c1 + 1
        if d == 1:  # →
            if c2 == m - 1:
                return [r1, 0, r1 + h - 1, w - 1]
            return [r1, c1 + 1, r2, c2 + 1]
        if d == 3:  # ←
            if c1 == 0:
                return [r1, m - w, r1 + h - 1, m - 1]
            return [r1, c1 - 1, r2, c2 - 1]
        if d == 2:  # ↓
            if r2 == n - 1:
                return [0, c1, h - 1, c1 + w - 1]
            return [r1 + 1, c1, r2 + 1, c2]
        # ↑
        if r1 == 0:
            return [n - h, c1, n - 1, c1 + w - 1]
        return [r1 - 1, c1, r2 - 1, c2]

    # 경계까지만 레이캐스트(랩 X): 같은 줄에서 '가장 가까운' 앱
    def ray_neighbors(aid, d, rect, bd):
        r1, c1, r2, c2 = rect[aid]
        ngb = set()
        if d == 1:  # →
            for r in range(r1, r2 + 1):
                for c in range(c2 + 1, m):
                    v = bd[r][c]
                    if v and v != aid:
                        ngb.add(v)
                        break
        elif d == 3:  # ←
            for r in range(r1, r2 + 1):
                for c in range(c1 - 1, -1, -1):
                    v = bd[r][c]
                    if v and v != aid:
                        ngb.add(v)
                        break
        elif d == 2:  # ↓
            for c in range(c1, c2 + 1):
                for r in range(r2 + 1, n):
                    v = bd[r][c]
                    if v and v != aid:
                        ngb.add(v)
                        break
        else:  # ↑
            for c in range(c1, c2 + 1):
                for r in range(r1 - 1, -1, -1):
                    v = bd[r][c]
                    if v and v != aid:
                        ngb.add(v)
                        break
        return ngb

    # 이번 '한 칸'의 목적지와 '겹치는' 앱들(랩 여부와 무관하게 항상 체크)
    def overlap_neighbors(aid, d, rect, bd):
        ngb = set()
        dr = dest_rect(rect[aid], d)
        r1, c1, r2, c2 = dr
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                v = bd[r][c]
                if v and v != aid:
                    ngb.add(v)
        return ngb

    # 명령 실행
    rect = collect_rects(board)
    for aid, d in commands:
        # 혹시 없는 id면 스킵
        if aid not in rect:
            continue

        # 1) 연쇄 집합(클로저)
        to_move = {aid}
        changed = True
        while changed:
            changed = False
            add = set()
            for x in list(to_move):
                add |= ray_neighbors(x, d, rect, board)          # 경계까지 레이캐스트
                add |= overlap_neighbors(x, d, rect, board)       # 목적지 겹침(랩 포함)
            new = add - to_move
            if new:
                to_move |= new
                changed = True

        # 2) 좌표만 동시에 갱신
        for x in to_move:
            rect[x] = dest_rect(rect[x], d)

        # 3) 보드 전체 재구성
        board = [[0] * m for _ in range(n)]
        for x, (r1, c1, r2, c2) in rect.items():
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    board[r][c] = x

    return board



print(solution(
[[0, 2, 2, 0, 0, 0, 0, 0], [0, 2, 2, 0, 0, 4, 4, 0], [0, 3, 3, 3, 1, 4, 4, 0], [0, 3, 3, 3, 0, 0, 0, 0], [0, 3, 3, 3, 5, 5, 6, 0], [0, 0, 0, 0, 5, 5, 0, 0]], [[3, 1], [3, 1]]))
#[[0, 0, 2, 2, 0, 0, 0, 0], [4, 4, 2, 2, 0, 0, 0, 0], [4, 4, 0, 3, 3, 3, 1, 0], [0, 0, 0, 3, 3, 3, 0, 0], [6, 0, 0, 3, 3, 3, 5, 5], [0, 0, 0, 0, 0, 0, 5, 5]]

print(solution([[0, 9, 1, 1, 6, 0, 0, 0], [2, 2, 1, 1, 0, 0, 0, 0], [2, 2, 3, 4, 4, 4, 0, 0], [5, 0, 0, 4, 4, 4, 7, 0], [0, 0, 0, 4, 4, 4, 8, 8], [0, 0, 0, 0, 0, 0, 8, 8]], [[2, 1], [3, 1], [9, 2], [4, 1]] ))
#[[8, 8, 0, 1, 1, 6, 0, 0], [8, 8, 0, 1, 1, 0, 0, 0], [4, 4, 4, 9, 3, 0, 0, 0], [4, 4, 4, 7, 2, 2, 0, 0], [4, 4, 4, 0, 2, 2, 0, 0], [0, 5, 0, 0, 0, 0, 0, 0]]

print(solution([[1, 1, 0], [1, 1, 0]], [[1, 4], [1, 3], [1, 2]]))
#[[0, 1, 1], [0, 1, 1]