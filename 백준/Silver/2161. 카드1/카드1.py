n=int(input())
numbers = [i for i in range(1,n+1)]
# print(numbers)
t = []
while(len(numbers)>0):
  try:
    # t.append(numbers[0])
    print(numbers[0],end=" ")
    del numbers[0]    
    # print(numbers)
    numbers.append(numbers[0]) #맨뒤에 붙이기
    del numbers[0] 
  except IndexError:
  # print("IndexError: List index out of range")
    break
# print(numbers)