for test_case in range(10):
    n = input().strip()
    if n == "...":
        break
    n = int(n)

    numlist = list(map(int,input().split()))
    answer = 0
    k = 5

    for i in range(2, n-2):

        m = max(numlist[i-2], numlist[i-1], numlist[i+1], numlist[i+2]) #양옆 4개 중 최대값
        # print(numlist[i],m)

        if numlist[i] - m > 0: #최대값이랑 내 위치랑의 차
            answer += (numlist[i]-m)

    print(f'#{test_case+1} {answer}')
