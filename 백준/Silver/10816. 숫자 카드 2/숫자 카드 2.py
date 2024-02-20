from collections import Counter

n=int(input())
n_array= list(map(int,input().split()))

m=int(input())
m_array=list(map(int,input().split()))

count = Counter(n_array)

for i in m_array:
    if i in count:
        print(count[i], end = " ")
    else: 
        print(0, end=" ")