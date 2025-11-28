# isbn

n = list(input())
# print(n)

# print(n.index('*')+1)
# m = 10 - (a+3b+c+3d+e+3f+g+3h+i+3j+k+3l) mod 10
# 다 더함 % 10 ==0
# 다 더함이 10의 배수가 될 수 있게

answer = 0

for i in range(12):
    if n[i].isdigit():
        if (i+1)%2==0: #짝수면 *3
            answer += int(n[i])*3
        else: #홀수면 1
            answer += int(n[i])
        # print(i,answer)
answer += int(n[-1])

# print(answer)

if (n.index("*")+1) % 2 ==0:
    result =  10 - (answer%10)
    b = 1
    for i in range(10):
        if (b*3)%10 == result:
            break
        else:
            b+=1
    if result == 10 :
        print(0)
    else:
        print(b)

else:
    result = 10-(answer%10)
    if result == 10:
        print(0)
    else:
        print(result)
