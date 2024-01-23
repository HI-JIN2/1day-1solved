si = 1
while True:
    n = int(input())
    name_list = []
    values = []

    for i in range(n):
        name = input()
        name_list.append(name)

    try:
        for i in range(2 * n - 1):
            a = int(input().split()[0].lstrip('0'))
            if a == 0:
                break
            if a not in values:
                values.append(a)
            elif a in values:
                values.remove(a)
            values.sort()

        print(si, name_list[values[0]-1])
        si += 1

    except IndexError:
        # print("IndexError: List index out of range")
        break
