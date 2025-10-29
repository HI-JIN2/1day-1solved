def solution(numbers, hand):
    answer = ''
    
    left = ['*',7,4,1]
    right = ['#',9,6,3]
    others = [0,8,5,2]
    
    l,r = (0,0), (0,0)
    #인덱스 1은 현재 손이 가운데있음
        
    for i in numbers:
        # print(left[l[0]],right[r[0]],i)
        if i in left:
            answer+='L'
            l = (left.index(i),0)
            
        elif i in right:
            answer += 'R'
            r = (right.index(i),0)
        
        else: 
            # print(left[l[0]],right[r[0]],i)
            idx = others.index(i)
            # print("왼",abs(idx-l[0])+l[1],"오", abs(idx-r[0])+r[0])
            dist = (abs(idx-l[0])+l[1]) - (abs(idx-r[0])+r[1])
            
            if dist>0:#왼에서 오 뺀게 양수면 오른쪽이 최단거리
                answer +="R"
                r = (others.index(i),-1)
            elif dist<0: 
                answer +="L"    
                l = (others.index(i),-1)
            else: #같다면
                if hand == "right":
                    answer +="R"
                    r = (others.index(i),-1)
                else:
                    answer +="L"    
                    l = (others.index(i),-1)
    return answer