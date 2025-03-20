n=int(input())
score = list(map(int,input().split()))
n_score =list()

t=max(score)

for i in score:
    n_score.append(i/t*100)

sum=0

for i in n_score:
    sum +=i

print(sum/n)