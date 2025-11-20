origin = "abcdefghijklmnopqrstuvwxyz"
# change = "wghuvijxpqrstacdebfklmnoyz"


n = int(input())
for i in range(n):
    cnt = {}

    for c in origin:
        cnt[c] =0 #초기화

    data = input()

    for d in data:
        if d.isalpha():
            cnt[d] +=1

    # print(cnt)
    max_keys = [k for k in cnt if cnt[k] == max(cnt.values())]
    if len(max_keys) == 1:
        print(max_keys[0])
    else:
        print("?")
        