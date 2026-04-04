n = int(input())

for _ in range(n):
    a,b = map(str,input().split())

    a_list = list(a)

    b_list = list(b)

    possible = True

    #a랑 b랑 길이가 다른 테케가 있을거라고 상상도 못함
    if len(a_list) != len(b_list):
        possible = False

    for b in b_list:
        if b in a_list:
            a_list.remove(b)
        elif b not in a_list:
            possible = False

    if possible:
        print("Possible")
    else:
        print("Impossible")
