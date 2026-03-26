data = list(input())
alpha = [0]*26

for d in data:
    alpha[ord(d)-97]+=1

for a in alpha:
    print(a, end=" ")