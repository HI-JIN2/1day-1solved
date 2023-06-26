def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)): #차피 1개가 남으니까 completion의 개수만큼 해도 됨
        if participant[i] != completion [i]: #participant에 없는 값이면 그걸 반환
            return participant[i]
    else:
        return participant[-1] #completion의 개수 만큼 돌았으니까 하나 남은건 당연히 이거임

