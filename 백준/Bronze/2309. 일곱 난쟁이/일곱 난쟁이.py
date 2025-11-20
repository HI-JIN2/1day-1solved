from itertools import combinations

tiny = []
for i in range(9):
    tiny.append(int(input()))
# print(tiny)
tiny.sort()


#합이 100이 되게
for i in combinations(tiny,7):
    total = sum(i)

    if total == 100:
        for j in i:
            print(j)
        exit()