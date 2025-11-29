t = int(input())
for test_case in range(t):
    n = int(input())
    a, b = 1, 0 # 0과 1이 호출된 횟수
    
    # n=0, 1 0
    # n=1, 0 1
    # n=2, 1,1
    # n=3, 1,2
    for i in range(n):
        # 0은 1이 호출된 횟수만큼, 1은 0과 1이 호출된 합만큼 출력됨
        a,b = b, a+b 
    print(a,b)
