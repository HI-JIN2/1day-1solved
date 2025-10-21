# 0시 0분 0초 ~ N시 59분 59초까지
# 3이 하나라도 포함하는 모든 경우



# def solution(n):
#     answer = 0
#
#     for i in range(n+1):
#         print(i)
#         if n%10 == 3: #나머지 3이면
#             answer += 60*60
#             print(60*60)
#         else:
#             answer += 6*6
#             print(6*6)
#
#     return answer

def solution(n):
    answer = 0

    # 완전탐색
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                now = str(i)+str(j)+str(k) #00시 20분 30초를 002030으로 만듦
                if '3' in now:
                    answer+=1

    return answer


print(solution(5))
