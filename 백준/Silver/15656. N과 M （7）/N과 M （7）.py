# 같은 숫자를 여러번 골라도됨

n, m = map(int, input().split())
nlist = list(map(int,input().split()))

s = []
nlist = sorted(nlist)

def fun():
    if len(s) == m:
        print(*s)
        return

    for i in range(n):
        s.append(nlist[i])

        fun()

        s.pop()

fun()