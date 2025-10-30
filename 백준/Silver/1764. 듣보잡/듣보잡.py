import sys
input = sys.stdin.readline

n,m = map(int,input().split())
names = {}

for i in range(n):
    names[input().strip()] = 1

# new_names = []
for j in range(m):
    name = input().strip()
    if name in names:
        names[name]+=1

# new_names.sort()
# print(len(names))
key = list(names.keys())
key.sort()

answer = []
for i in key:
    if names[i]==2:
        answer.append(i)

print(len(answer))
for i in answer:
    print(i)