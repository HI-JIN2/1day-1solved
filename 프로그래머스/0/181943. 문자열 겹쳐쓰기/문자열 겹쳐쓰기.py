def solution(my_string, overwrite_string, s):
    
    my_l = len(my_string)
    o_l=len(overwrite_string)
    print(my_l,o_l)
    
    
    answer = my_string[:s]+    overwrite_string + my_string[s+o_l:]
    # if(ori>len(answer) ):
        # answer = answer+ my_string[l+2:]
    
    # answer = ''
    return answer