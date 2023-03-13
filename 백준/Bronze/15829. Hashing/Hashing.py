L = int(input())
string = input()
sum=0

for i in range(L):
    sum += (ord(string[i])-96) * (31 ** i)
print(sum % 1234567891)