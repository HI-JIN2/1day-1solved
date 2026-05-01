def solution(n, words):
    answer = []
    
    arr = []
    for i in range(len(words)//n+1): #누가
        for j in range(n): #몇번째에
            # print(i,j, words[i*n+j])
            #이전에 없는가
            #끝말이 맞는가
            if i*n+j >= len(words):
                continue
            elif i*n+j == 0:
                arr.append(words[i*n+j])
            elif words[i*n+j] not in arr and words[i*n+j-1][-1] == words[i*n+j][0]:
                arr.append(words[i*n+j])
            else:

                return [j+1,i+1]
                
                
    if len(answer)==0:
        return [0,0]
