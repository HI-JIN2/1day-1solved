#능력치 차이를 최소로
from itertools import combinations

n = int(input())

s = []
for i in range(n):
    s.append(list(map(int,input().split())))
# print(s)

answer = []

def get_score(team):
    total = 0
    for i in range(len(team)):
        for j in range(i+1,len(team)):
            total += s[team[i]][team[j]] + s[team[j]][team[i]]
    return total

for team in combinations(range(n), n//2):
    other_team = [i for i in range(n) if i not in team]

    diff = abs(get_score(team) - get_score(other_team))
    answer.append(diff)

answer.sort()
print(answer[0])
