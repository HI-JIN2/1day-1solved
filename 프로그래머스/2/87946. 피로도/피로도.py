def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)

    def dfs(current_k, count):
        nonlocal answer

        answer = max(answer, count)

        for i in range(len(dungeons)):
            need, cost = dungeons[i]

            # 아직 안 갔고, 현재 피로도가 최소 필요 피로도 이상이면 갈 수 있음
            if not visited[i] and current_k >= need:
                visited[i] = True

                dfs(current_k - cost, count + 1)

                visited[i] = False

    dfs(k, 0)

    return answer