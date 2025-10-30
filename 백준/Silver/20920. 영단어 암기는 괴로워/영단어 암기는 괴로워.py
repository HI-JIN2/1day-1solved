import sys
input = sys.stdin.readline

n, m = map(int,input().split())
dict = {}
for i in range(n):
    word = input().strip()
    if len(word)>=m:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

#-는 내림차순을 의미. -x[1] 단어 빈도수 높은순서대로,
# -len[x[0]] 단어 길이 높은 순서대로
# x[0] 알파벳순

wordlist = sorted(dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for word, cnt in wordlist:
    print(word)
