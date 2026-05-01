from collections import defaultdict 
def solution(want, number, discount):
    answer = 0
    
    shop = defaultdict(int)
    
    for w, n in zip(want,number):
        shop[w] += n
        
    # print(shop)
    
    l = len(discount)-9
    for i in range(len(discount)): #14개라면 
        
        slist = shop.copy() #복사
        
        for s in slist.keys(): 
            if s in discount[i:i+10] and slist[s]>0 and slist[s] == discount[i:i+10].count(s):
                slist[s] = 0
        # print(slist)
        if sum(slist.values()) == 0:
            answer+=1
        
    
    return answer