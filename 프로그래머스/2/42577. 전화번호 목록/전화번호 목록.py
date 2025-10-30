# def solution(phone_book):
#     answer = True
#     cnt = 0
    
#     sphone_book = sorted(phone_book, key = lambda x: len(x))
#     shortest = sphone_book[0]
    
#     for number in phone_book:
#         # print(number,"==")
        
#         if number == shortest:
#             continue
            
#         for i in range(len(shortest)):
#             if shortest[i] == number[i]:
#                 # print(number[i], "같아")
#                 cnt+=1
                
#         if cnt == len(shortest):
#             return False
#         else:
#             cnt = 0
    
#     return answer

def solution(phone_book):
    answer = True
    cnt = 0
    
    phone_book.sort()
    
    
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1]:
            continue
        # print(phone_book[i],phone_book[j])

        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return answer