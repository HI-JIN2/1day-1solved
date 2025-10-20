# N =5
# 각 모험가의 공포도  2 3 1 2 2   -> 2

# 그룹의 최대 수

n = int(input())
m = list(map(int,input().split()))
m.sort()
print(m)
# 오름차순으로 정렬 1 2 2 2 3
# 오름차순으로 해야 최소한의 모험가만 포함해서 그룹을 만듦으로 그룹수를 최대로 만들 수 있음

cnt =0 #그룹 안의 모험가 수
result =0 #그룹 수

for i in m:
    print(i)
    cnt +=1
    if cnt >=i: #현재 그룹에 있는 모험가 수가 공포도 이상이라면 여행을 갈 수 있음
        result +=1
        cnt =0
        print("초기화")

print("===")

print(result)