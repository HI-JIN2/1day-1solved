def solution(num_list):
    hap =0
    gop=1
    for i in num_list:
        hap+=i
        gop*=i
    
    if hap**2>gop:
        return 1
    else:
        return 0
