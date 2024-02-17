n=input()

array=[]
for i in n:
    array.append(i)

array.sort(reverse=True)
# print(array)

for i in array:
    print(i,end="")