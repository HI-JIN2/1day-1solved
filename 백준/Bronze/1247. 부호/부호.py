import sys

for _ in range(3):
    sum = 0
    n = int(sys.stdin.readline().strip())
    for x in range(n):
        num = int(sys.stdin.readline().strip())
        sum += num
    if sum > 0:
        print("+")
    elif sum < 0:
        print('-')
    else:
        print("0")