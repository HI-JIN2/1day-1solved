n = int(input())
dict = {}

answer = 0
for i in range(n):
    a,b = map(int,input().split())
    #소 번호, 소 위치


    if a not in dict:
        dict[a] = b

    else:
        if dict[a] != b: #이전 길이랑 다르면 +1
            # print(a,b,dict[a])
            dict[a] = b
            answer += 1

print(answer)

