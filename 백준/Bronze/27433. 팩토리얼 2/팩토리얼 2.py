n=int(input())
s=1

for _ in range(n):
    s=s*n
    n=n-1
    
print(s)