from collections import deque

def solution(n, start, edges, k):
    # 1️⃣ 파이프 종류별 그래프 만들기
    graph = {1: [[] for _ in range(n + 1)],
             2: [[] for _ in range(n + 1)],
             3: [[] for _ in range(n + 1)]}

    for a, b, t in edges:
        graph[t][a].append(b)
        graph[t][b].append(a)

    # 2️⃣ 파이프 종류별 연결된 그룹(컴포넌트) 찾기
    groups = {1: [], 2: [], 3: []}
    belong = {1: [None]*(n+1), 2: [None]*(n+1), 3: [None]*(n+1)}

    def bfs_find_groups(pipe_type):
        visited = [False]*(n+1)
        for i in range(1, n+1):
            if not visited[i]:
                q = deque([i])
                visited[i] = True
                group = [i]
                while q:
                    now = q.popleft()
                    for nxt in graph[pipe_type][now]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)
                            group.append(nxt)
                groups[pipe_type].append(group)
                for node in group:
                    belong[pipe_type][node] = len(groups[pipe_type]) - 1

    for t in (1, 2, 3):
        bfs_find_groups(t)

    # 3️⃣ DFS + 메모이제이션
    memo = {}

    def dfs(steps, infected):
        key = (steps, tuple(sorted(infected)))
        if key in memo:
            return memo[key]

        best = len(infected)
        if steps == 0:
            memo[key] = best
            return best

        for t in (1, 2, 3):
            new_infected = set(infected)  # deepcopy 불필요!
            touched = set()
            for node in infected:
                group_idx = belong[t][node]
                if group_idx is not None and group_idx not in touched:
                    touched.add(group_idx)
                    for v in groups[t][group_idx]:
                        new_infected.add(v)
            best = max(best, dfs(steps - 1, new_infected))

        memo[key] = best
        return best

    return dfs(k, {start})

# from collections import deque
#
# def solution(n, infection, edges, k):
#     # 1) 파이프 종류별 인접 리스트
#     adj_by_type = {1: [[] for _ in range(n + 1)],
#                    2: [[] for _ in range(n + 1)],
#                    3: [[] for _ in range(n + 1)]}
#     for x, y, type in edges:
#         adj_by_type[type][x].append(y)
#         adj_by_type[type][y].append(x)
#
#     # 2) 파이프 종류별 연결 컴포넌트(한 번에 열리는 구간)
#     comp_mask_by_node = {1: [0]*(n+1), 2: [0]*(n+1), 3: [0]*(n+1)}
#
#     def build_components(pipe_type):
#         seen = [False]*(n+1)
#         for s in range(1, n+1):
#             if not seen[s]:
#                 if not adj_by_type[pipe_type][s]:
#                     seen[s] = True
#                     comp_mask_by_node[pipe_type][s] = 1 << (s-1)
#                     continue
#                 q = deque([s])
#                 seen[s] = True
#                 nodes = [s]
#                 while q:
#                     u = q.popleft()
#                     for v in adj_by_type[pipe_type][u]:
#                         if not seen[v]:
#                             seen[v] = True
#                             q.append(v)
#                             nodes.append(v)
#                 mask = 0
#                 for v in nodes:
#                     mask |= 1 << (v-1)
#                 for v in nodes:
#                     comp_mask_by_node[pipe_type][v] = mask
#
#     for t in (1, 2, 3):
#         build_components(t)
#
#     # 3) 특정 파이프 종류(type)를 열었을 때 감염 확장
#     def expand(mask, pipe_type):
#         m = mask
#         new_mask = mask
#         seen_comp = set()
#         while m:
#             lsb = m & -m
#             v = (lsb.bit_length() - 1) + 1
#             comp = comp_mask_by_node[pipe_type][v]
#             if comp and comp not in seen_comp and (comp & mask):
#                 seen_comp.add(comp)
#                 new_mask |= comp
#             m ^= lsb
#         return new_mask
#
#     # 4) DFS + 메모이제이션 없이 직접 캐시
#     memo = {}
#     start_mask = 1 << (infection - 1)
#
#     def dp(steps_left, mask):
#         key = (steps_left, mask)
#         if key in memo:
#             return memo[key]
#
#         best = bin(mask).count('1')
#         if steps_left == 0:
#             memo[key] = best
#             return best
#
#         for pipe_type in (1, 2, 3):
#             nxt = expand(mask, pipe_type)
#             best = max(best, dp(steps_left - 1, nxt))
#
#         memo[key] = best
#         return best
#
#     return dp(k, start_mask)

# from collections import defaultdict, deque
#
# def solution(n, infection, edges, k):
#     # 1) 색별 인접 리스트
#     adj_by_color = {1: [[] for _ in range(n + 1)],
#                     2: [[] for _ in range(n + 1)],
#                     3: [[] for _ in range(n + 1)]}
#     for x, y, t in edges:
#         adj_by_color[t][x].append(y)
#         adj_by_color[t][y].append(x)
#
#     # 2) 색별 컴포넌트(비트마스크) 계산
#     # comp_mask_by_node[c][v] = v가 속한 c색 컴포넌트의 비트마스크(int)
#     comp_mask_by_node = {1: [0]*(n+1), 2: [0]*(n+1), 3: [0]*(n+1)}
#
#     def build_components(color):
#         seen = [False]*(n+1)
#         for s in range(1, n+1):
#             if not seen[s]:
#                 if not adj_by_color[color][s]:   # 간선이 없어도 "자기 자신만"인 컴포넌트
#                     seen[s] = True
#                     comp_mask_by_node[color][s] = 1 << (s-1)
#                     continue
#                 # BFS/DFS로 컴포넌트 수집
#                 q = deque([s])
#                 seen[s] = True
#                 nodes = [s]
#                 while q:
#                     u = q.popleft()
#                     for v in adj_by_color[color][u]:
#                         if not seen[v]:
#                             seen[v] = True
#                             q.append(v)
#                             nodes.append(v)
#                 # 비트마스크로 기록
#                 mask = 0
#                 for v in nodes:
#                     mask |= 1 << (v-1)
#                 for v in nodes:
#                     comp_mask_by_node[color][v] = mask
#
#     build_components(1)
#     build_components(2)
#     build_components(3)
#
#     # 3) 한 번 색 c를 열었을 때의 확장 함수
#     def expand(mask, color):
#         # mask에 들어있는 노드들이 속한 'color' 컴포넌트들을 모두 합집합
#         m = mask
#         new_mask = mask
#         seen_comp = set()  # 같은 컴포넌트를 중복 OR 하지 않기 위해
#         while m:
#             lsb = m & -m
#             v = (lsb.bit_length() - 1) + 1  # 노드 번호(1-index)
#             comp = comp_mask_by_node[color][v]
#             if comp not in seen_comp and (comp & mask):  # 교집합 있으면 전부 퍼짐
#                 seen_comp.add(comp)
#                 new_mask |= comp
#             m ^= lsb
#         return new_mask
#
#     # 4) DP: (steps_left, mask) -> 최대 감염 수
#     from functools import lru_cache
#
#     start_mask = 1 << (infection - 1)
#
#     @lru_cache(None)
#     def dp(steps_left, mask):
#         # 더 진행하지 않아도 되는 선택 허용
#         best = bin(mask).count('1')
#         if steps_left == 0:
#             return best
#         for color in (1, 2, 3):
#             nxt = expand(mask, color)
#             if nxt != mask:  # 변화가 있을 때만 의미 있음
#                 best = max(best, dp(steps_left - 1, nxt))
#             else:
#                 # 변화가 없어도 색을 바꿔야 더 늘릴 수 있을 수 있음
#                 # (예: 이번엔 의미 없지만 다음 색 전환으로 증가)
#                 best = max(best, dp(steps_left - 1, mask))
#         return best
#
#     return dp(k, start_mask)

print(solution(10, 1, [[1, 2, 1], [1, 3, 1], [1, 4, 3], [1, 5, 2], [5, 6, 1], [5, 7, 1], [2, 8, 3], [2, 9, 2], [9, 10, 1]], 2))
print(solution(7, 6, [[1, 2, 3], [1, 4, 3], [4, 5, 1], [5, 6, 1], [3, 6, 2], [3, 7, 2]], 3))