n = int(input())
data = []
answer = 0
endtime = 0 #현재 잡힌 회의가 끝나는 시간

for _ in range(n):
    start, end = map(int,input().split())
    data.append((start,end))
data.sort(key = lambda x: (x[1], x[0]))
# print(data)

for t in data:
    start, end = t

    if start >= endtime: #뉴 타깃이 현재 잡힌 회의가 끝나고 나서 시작하면
        #끝나자마자 다른 회의 시작할 수 있으니까 등호
        answer +=1 # 개수 더하고
        endtime = end #현재 잡힌 회의가 끝날 시간을 바꿔줌

print(answer)