n = int(input())
switch = list(map(int,input().split()))
switch_cnt = len(switch)

student_cnt = int(input())
student = []
for i in range(student_cnt):
    a,b = map(int,input().split())
    student.append((a,b))
# print(student)

for s in student:
    if s[0] == 1: #남학생
        # print("남학생")
        for j in range(1,switch_cnt+1):
            if j % s[1] ==0 :
                if switch[j-1] ==0:
                    switch[j-1] = 1
                else:
                    switch[j-1] =0
    else: #여학생
        # print("여학생")
        tmp = min(s[1]-1,switch_cnt-s[1])
        # print(tmp)
        # print(switch)
        for k in range(tmp+1):
            # print(k)
            # print(switch)
            if switch[s[1]-k-1] == 0 and switch[s[1]+k-1] ==0 :
                # print("0으로 같습니다 ")
                switch[s[1] - k-1] = 1
                switch[s[1] + k-1] = 1

            elif switch[s[1]-k-1] == 1 and switch[s[1]+k-1] ==1:
                switch[s[1] - k-1] = 0
                switch[s[1] + k-1] = 0
                # print("1로 같습니다")

            # print("데",switch)

# print(switch)
for i in range(1, switch_cnt+1):
    print(switch[i-1], end=" ")
    if i%20 == 0 :
        print()