n = int(input())
target = ""
for i in range(n):
    target += "IO"
target += "I"
# print(target)

m = int(input())
s = list(input().strip())

answer = 0
for i in range(m-len(target)+1):
    temp = 0
    # print("i===",i)
    for j in range(i,i+len(target)):
        # print("j",s[j],temp)
        if s[j] == target[j-i]:
            temp +=1
        else:
            temp = 0
    if temp == len(target):
        answer +=1
print(answer)