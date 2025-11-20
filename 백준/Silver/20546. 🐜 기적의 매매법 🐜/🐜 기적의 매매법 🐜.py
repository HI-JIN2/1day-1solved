money = int(input())
price = list(map(int,input().split()))

jh = 0
jh_money = money
sm_money = money
jh_cnt = 0 #준현이 보유주식수
for i in range(len(price)):
    # print(i,"일차")

    if jh_money>=price[i]:
        today_buy_cnt = jh_money // price[i] #매수 가능 주식수
        # print(today_buy_cnt)
        jh_cnt += today_buy_cnt
        # print(jh_cnt)
        jh_money -= price[i] * today_buy_cnt #남은현금
        # print(jh_money)
    # print(price[i], jh_money,jh_cnt )
jh_result = jh_money+price[-1]*jh_cnt
# print(jh_result)


flag = 0 #2가 상승 1이 하락
day_cnt_up = 0
day_cnt_down = 0
sm_cnt = 0 #성민이 보유주식수
for i in range(1,len(price)-1):
    # if sm_money>=price[i]: #전량 매수
    #     today_buy_cnt = sm_money // price[i]  # 매수 가능 주식수
    #     sm_cnt += today_buy_cnt
    #     sm_money -= price[i] * today_buy_cnt #남은현금

    # print(i,"일차== 현재 현금",sm_money,"현재 주식수",sm_cnt )

    # print( price[i-1],price[i])
    if price[i-1]<price[i]: #상승
        day_cnt_up+=1
        # print("상승", day_cnt_up,"일차")
        if flag == 1 :
            day_cnt_up =1
        if flag==2 and day_cnt_up ==3: #3일째 되면 전량 매도
            if sm_cnt != 0 :
                sm_money = price[i+1] * sm_cnt
                sm_cnt = 0
            day_cnt_up = 0 #3일 법칙 리셋

        flag = 2
        day_cnt_down = 0

    else: #하락
        day_cnt_down+=1
        # print("하락", day_cnt_down,"일차")

        if flag == 1 and day_cnt_down == 3:
            today_buy_cnt = sm_money // price[i]  # 매수 가능 주식수
            sm_cnt += today_buy_cnt
            # print(sm_money, price[i],today_buy_cnt,"만큼",price[i] * today_buy_cnt)
            sm_money -= price[i] * today_buy_cnt  # 남은현금
            day_cnt_down = 0 #3일 법칙 리셋

        if flag == 2  :
            day_cnt_down = 1
        flag =1
        day_cnt_up = 0

sm_result = sm_money+price[-1]*sm_cnt
# print(sm_money, price[-1],sm_cnt)
# print(sm_result)


if jh_result>sm_result:
    print("BNP")
elif jh_result<sm_result:
    print("TIMING")
else:
    print("SAMESAME")