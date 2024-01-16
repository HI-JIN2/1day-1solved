a,b,c= map(int,input().split())
d=int(input())

a_=d//3600
b_=(d%3600)//60 #분
c_=(d%3600)%60

a+=a_
b+=b_
c+=c_

# print(a_,b_,c_)
if c>=60:
  c-=60
  b+=1
if b>=60:
  b-=60
  a+=1
while(a>=24):
  a-=24

print(a,b,c)
