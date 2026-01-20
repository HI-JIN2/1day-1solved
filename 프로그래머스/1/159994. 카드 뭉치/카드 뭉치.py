
def solution(cards1, cards2, goal):
    l = []
    answer = ""
    
    n = len(cards1)
    m = len(cards2)
    i = j = 0
    
    for word in goal:
        if i<n and word ==cards1[i]:
            l.append(word)
            i+=1
        if j<m and word == cards2[j]:
            l.append(word)
            j+=1
    
    if l == goal:
        return "Yes"
    else:
        return "No"
