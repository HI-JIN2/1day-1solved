def solution(survey, choices):
    personality_dict={"A":0,"N":0,"C":0,"F":0,"M":0,"J":0,"R":0,"T":0}
    for i, j in zip(survey, choices):
        if j>4:
            personality_dict[i[1]] = personality_dict[i[1]] + (j-4)
        else:
            if j==1:
                personality_dict[i[0]] = personality_dict[i[0]] + 3
            if j==2:
                personality_dict[i[0]] = personality_dict[i[0]] + 2
            if j==3:
                personality_dict[i[0]] = personality_dict[i[0]] + 1
                
    
    answer = ''
    if personality_dict['R'] >= personality_dict['T']:
        answer = answer + 'R'
    elif personality_dict['R'] < personality_dict['T']:
        answer = answer + 'T'
    
    if personality_dict['C'] >= personality_dict['F']:
        answer = answer + 'C'
    elif personality_dict['C'] < personality_dict['F']:
        answer = answer + 'F'
        
    if personality_dict['J'] >= personality_dict['M']:
        answer = answer + 'J'
    elif personality_dict['J'] < personality_dict['M']:
        answer = answer + 'M'
        
    if personality_dict['A'] >= personality_dict['N']:
        answer = answer + 'A'
    elif personality_dict['A'] < personality_dict['N']:
        answer = answer + 'N'
    return answer