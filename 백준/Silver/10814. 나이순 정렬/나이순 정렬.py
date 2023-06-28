import sys
N= int(sys.stdin.readline())


closet = dict() 
for i in range(N): 
    year,name=sys.stdin.readline().split(" ")
    year=int(year)
    if year in closet: closet[year].append(name) 
    else: closet[year] = [name] ##


for key,value in sorted(closet.items()):
    for i in range(len(value)):
        print(f"{key} {value[i]}",end="")