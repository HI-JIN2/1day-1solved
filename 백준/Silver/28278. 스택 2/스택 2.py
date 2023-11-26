import sys


n = int(input())

a = []

for _ in range(int(n)):
    command = sys.stdin.readline().split()

    if command[0] == '1':
        c = int(command[1])
        a.append(c)
    elif command[0] == '2':
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop())
    elif command[0] == '3':
        print(len(a))
    elif command[0] == '4':
        print(1 if len(a) == 0 else 0)
    elif command[0] == '5':
        if len(a) == 0:
            print(-1)
        else:
            print(a[-1])
