word1 = list(input())
word2 = list(input())

word22 = word2.copy()
answer = 0

for i in list(word1):
    if i in word22:
        word22.remove(i)
# print(word22)
answer += len(word22)

for i in list(word2):
    if i in word1:
        word1.remove(i)
# print(word1)
answer += len(word1)

print(answer)