import sys

n,b = map(int,sys.stdin.readline().rstrip().split())
letter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s=""

while n:
    s += str(letter[n%b])
    n //= b

print(s[::-1])
