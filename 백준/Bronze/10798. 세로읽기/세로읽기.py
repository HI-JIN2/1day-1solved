data = [ ]

for i in range(5):
    data.append(list(input().strip()))
# print(data)

longest = 0
for i in data:
    longest = max(longest, len(i))
# print(longest)

answer = ''

for j in range(longest):
    for i in range(5):
        if j<len(data[i]):
            answer += data[i][j]

print(answer)