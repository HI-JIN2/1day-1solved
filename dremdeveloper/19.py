# 문자열 해싱을 이용한 검색 함수 만들기
#인데 딕셔너리로 풀기

def solution(string_list, query_list):
    answer = []

    dict = {}

    for i in query_list:
        dict[i] = 0

    # print(dict)

    for i in string_list:
        if i in dict:
            dict[i] = 1

    for i in dict.keys():
        if dict[i] ==1:
            answer.append(True)
        else: answer.append(False)

    return answer

print(solution(["apple","banana","cherry"],["banana","kiwi","melon","apple"]))