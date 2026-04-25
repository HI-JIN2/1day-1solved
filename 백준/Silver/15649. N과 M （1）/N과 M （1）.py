#n과 m 1
#백트래킹


n,m= map(int,input().split())

s = [] #수열

def fun():
    if len(s) == m:
        print(*s, sep=' ')
        return

    else:
        for i in range(1,n+1):
            if i not in s:
                s.append(i)
                fun()
                s.pop()

fun()