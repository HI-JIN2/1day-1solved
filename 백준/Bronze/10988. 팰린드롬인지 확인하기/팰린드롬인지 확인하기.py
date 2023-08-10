N=input()

# print(len(N))

# print(N[0])
# print(N[-1])

j=len(N)
if j ==1 :
    print("1")
else:
    for i in range(j//2):
        if(N[i] == N[j-i-1]): #0 -1 #1 -1
            # print(N[i],N[j-i-1])
            result=1
        else:
            # print(N[i],N[j-i-1])
            result=0
            break

    print(result)