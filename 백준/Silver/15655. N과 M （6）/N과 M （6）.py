n, m = map(int, input().split())
nlist = list(map(int,input().split()))

s = []
nlist = sorted(nlist)

def fun(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start,len(nlist)):
        if nlist[i] not in s:
            s.append(nlist[i])

            fun(i+1)

            s.pop()

fun(0) #인덱스