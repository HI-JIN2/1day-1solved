# 같은 숫자를 여러번 골라도됨

n, m = map(int, input().split())
nlist = list(map(int,input().split()))

s = []
nlist = sorted(nlist)

def fun(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start,n):
        s.append(nlist[i])

        fun(i)

        s.pop()

fun(0) #인덱스