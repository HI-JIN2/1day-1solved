p = int(input())
a, b, c, d = 0, 0, 0, 0
m_list = []
for _ in range(p):
  pay = int(input())
  # if m <= 500 & m >= 1:
  m_list.append(pay)

for pay in m_list:
  quarter = pay // 25
  dime = pay % 25 // 10
  nickel = pay % 25 % 10//5
  penny = pay % 5
  print(quarter, dime, nickel, penny)
