# n=int(input())
# score = list(map(int,input().split()))
# n_score =list()

# t=max(score)

# for i in score:
#     n_score.append(i/t*100)

# sum=0

# for i in n_score:
#     sum +=i

# print(sum/n)

#해설 풀이 수도코드
# n=int(input())
# score =list(map(int,input().split()))

# top=max(score)


# sum=0
# for i in score:
#     sum+=i


# print(sum/top*100/n)

# 해설풀이
n=int(input())
score=list(map(int,input().split()))
mymax=max(score)
sum=sum(score)


print(sum/n/mymax*100)