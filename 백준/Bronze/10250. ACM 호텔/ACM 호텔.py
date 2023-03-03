#H, W, N, 세 정수를 포함하고 있으며 각각 호텔의 층 수, 각 층의 방 수, 몇 번째 손님인지를 나타낸다
    

T = int(input())

for i in range(T):
    H, W, N, =map(int,input().split())
    c=N%H #나머지
    h= N//H +1 #목+1

    if(c==0 ):#나머지
        c=H
        h=N//H
    print(c*100+h)
    #print(str(c)+"0"+str(h))
    