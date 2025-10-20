n = int(input())
l = list(map(int,input().split()))
sum=0
sumLists=[]
if(n==1):
    l = sorted(l)
    for i in range(0,5):
        sum+=l[i]
else:
    sumLists.append(min(l[0],l[5]))
    sumLists.append(min(l[1],l[4]))
    sumLists.append(min(l[2],l[3]))
    sumLists = sorted(sumLists)

    #1,2,3면이 보여질때 주사위 최소값
    min1 = sumLists[0]
    min2 = sumLists[0] + sumLists[1]
    min3 = sumLists[0] + sumLists[1] + sumLists[2]

    #1,2,3면이 보여지는 주사위 개수
    n1 = (n-2)*(n-2) + 4*(n-1)*(n-2)
    n2 = 4*(n-2) + 4*(n-1)
    n3 = 4

    sum += n1 * min1
    sum += n2 * min2
    sum += n3 * min3

print(sum)