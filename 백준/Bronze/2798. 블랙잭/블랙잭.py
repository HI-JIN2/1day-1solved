#m을 넘지 않으면서 가장 가깝게

n,m = map(int,input().split())
card = list(map(int,input().split()))
card.sort(reverse=True)

hap_list = []

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            hap = card[i] + card[j]+ card[k]
            if hap > m:
                continue
            else:
                hap_list.append(hap)

print(max(hap_list))