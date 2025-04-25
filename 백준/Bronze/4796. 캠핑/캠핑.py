i=0
while True:
    l,p,v = map(int,input().split())
    if(l==p==v==0):
        break
    i+=1
    n = v//p
    answer= n*l+ v%p
    if v%p>l:
        answer = (v//p) * l + min(v%p, l) 
    print("Case {}: {}".format(i, answer))