N=int(input())
n1=N//100
n2=(N-n1*100)//10
n3=N%10
M=int(input())
m1=M//100
m2=(M-m1*100)//10
m3=M%10


print(N*m3)
print(N*m2)
print(N*m1)
print(N*M)