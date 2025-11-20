#
# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.

mo = ['a','e','i','o','u']

while True:
    data = input()
    flag1 = 0
    flag2 = 1
    flag3 = 1

    before = 0
    before_mo = 0
    before_ja = 0

    back = ''

    if data == 'end':
        exit()

    for i in data:
        if back == i:
            if i not in ['e', 'o']:
                flag3 = 0
                break

        if i in mo: #모음
            # print(i,"모음입니다")
            flag1+=1

            if before == 0: #전 값이 모음이야
                before_mo+=1

            else: #이전 값 모음 아님
                before = 0 #이전값을 모음으로 만들어주기
                before_mo=1 #누적개수 1로

            before = 0

        else: #자음
            if before == 1: #이전 값이 자음이면
                before_ja+=1
            else:  # 이전 값 자음 아님
                before = 1  # 이전값을 자음으로 만들어주기
                before_ja = 1  # 누적개수 1로
        back = i

        if before_mo>=3 or before_ja>=3:
            flag2=0
            break

    # print(before_mo, before_ja)
    # print(flag1,flag2,flag3)
    if flag1 and flag2 and flag3:
        print(f"<{data}> is acceptable.")
    else:
        print(f"<{data}> is not acceptable.")
