n, m = map(int, input().split())
nlist = list(map(int,input().split()))

s = []
nlist = sorted(nlist)

def fun():
    if len(s) == m:
        print(*s)
        return

    for i in range(n):
        if nlist[i] not in s:
            s.append(nlist[i])

            fun()

            s.pop()

fun()