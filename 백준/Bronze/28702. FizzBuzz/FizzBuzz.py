n1 = input()
n2 = input()
n3 = input()

nums = [n1,n2,n3]
answer =0


if nums[0] == "Fizz": #첫번째 수가 3의 배수일때
    for i in range(1,3):
        if nums[i].isdigit():
            answer = int(nums[i]) + 3 - i
            if answer % 5 == 0 :
                answer = "FizzBuzz"
            else:
                answer = "Fizz"
            break
# 첫 번째 수가 5의 배수 일때 처리
if nums[0] == 'Buzz' :
	for i in range(1, 3) :
		if nums[i].isdigit() :
			answer = int(nums[i]) + 3 - i
			if answer % 3 == 0 :
				answer = 'Fizz'
			break

if nums[0] == "Buzz": #첫번째 수가 5의 배수일때
    for i in range(1, 3):
        if nums[i].isdigit():
            answer = int(nums[i]) + 3 - i
            if answer % 3 == 0:
                answer = 'Fizz'
            break

if nums[0] == 'FizzBuzz':# 첫 번째 수가 15의 배수 일때 처리
    answer = 'Fizz'

if nums[0].isdigit() : # 첫 번째 수가 3의 배수, 5의 배수 모두 아닐때 처리
	answer = int(nums[0]) + 3
	if answer % 5 == 0 and answer % 3 == 0 :
		answer = 'FizzBuzz'
	elif answer % 5 == 0 :
		answer = 'Buzz'
	elif answer % 3 == 0 :
		answer = 'Fizz'

print(answer)
