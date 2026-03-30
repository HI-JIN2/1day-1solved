import math

answer = 0
card = [0]*10

data = list(map(int, input().strip()))
while data:
    num = data.pop()
    if num == 6:
        num =9
    card[num]+=1

# print(card)
nine = math.ceil(card[9]/2)
m =  max(card[:-1])
if m < nine:
    print(nine)
else:
    print(m)
