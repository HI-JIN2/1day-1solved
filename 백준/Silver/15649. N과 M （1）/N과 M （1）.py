n, m = map(int, input().split())

s = []
visited = [False] * (n + 1)

def fun():
    if len(s) == m:
        print(*s)
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            s.append(i)

            fun()

            s.pop()
            visited[i] = False

fun()