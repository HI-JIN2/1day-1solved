n=int(input())
score =list(map(int,input().split()))

top=max(score)


sum=0
for i in score:
    sum+=i


print(sum/top*100/n)