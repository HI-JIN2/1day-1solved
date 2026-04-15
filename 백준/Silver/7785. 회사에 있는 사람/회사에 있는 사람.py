from collections import defaultdict
t = int(input())
names = defaultdict(int)
for i in range(t):
    name, state = map(str,input().split())
    if state == "leave":
        names[name]=0
    elif state == "enter":
        names[name]=1

# print(names)
arr = []
for name,state in names.items():
    if state == 1:
        arr.append(name)

arr = sorted(arr, reverse = True)
print(*arr, sep="\n")