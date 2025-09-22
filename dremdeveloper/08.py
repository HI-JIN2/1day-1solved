# def solution(s):
#     list_s = list(s)
#
#     stack = []
#
#     for i in list_s:
#         stack.append(i)
#         if stack[-1] == "(":
#             continue
#         elif stack[-1] == ")" and stack[-2] == "(":
#             stack.pop()
#             stack.pop()
#
#     if len(stack) == 0:
#         return True
#     else:
#         return False

def solution(s):
    stack = []
    for i in s:
        if i =="(":
            stack.append(i)
        elif i == ")" and len(stack) != 0:
            stack.pop()
    if len(stack) == 0: return True
    else: return False

print("(())() is ",solution("(())()"))
print("((())() is ",solution("((())()"))
print("((( is ",solution("((("))
print("((() is ",solution("((()"))
print("()( is ",solution("()("))
print("() is ",solution("()"))
print(")( is ",solution(")("))

