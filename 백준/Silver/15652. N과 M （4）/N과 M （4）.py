n, m = map(int, input().split())

s = []
visited = [False] * (n + 1)

def fun(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start, n + 1):
        s.append(i)

        fun(i)

        s.pop()

fun(1)