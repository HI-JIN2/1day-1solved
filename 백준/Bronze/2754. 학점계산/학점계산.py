grade=input()
result=0.0

if grade[0]=="A":
    result=4.3
    if grade[1]=="0":
        result-=0.3
    elif grade[1]=="-":
        result-=0.6
elif grade[0]=="B":
    result=3.3
    if grade[1]=="0":
        result-=0.3
    elif grade[1]=="-":
        result-=0.6
elif grade[0] =="C":
    result=2.3
    if grade[1]=="0":
        result-=0.3
    elif grade[1]=="-":
        result-=0.6
elif grade[0]=="D":
    result=1.3
    if grade[1]=="0":
        result-=0.3
    elif grade[1]=="-":
        result-=0.6

print(round(result,1))
