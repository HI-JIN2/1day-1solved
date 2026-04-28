def solution(brown, yellow):
    answer = []
    n = brown+ yellow

    nlist = []    #약수 리스트
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            nlist.append(i)

            if i != n // i:
                nlist.append(n // i)

    # print(nlist)
    
    #
    for i in nlist:
        for j in nlist:
            if i-2>0 and j-2>0 and (i -2) * (j-2) == yellow:
                answer.append(i)
                answer.append(j)
                answer=sorted(answer, key = lambda x:-x)
                return answer