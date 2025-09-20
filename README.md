# 1일 1알고리즘
This is a auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).


### 파이썬 오답노트

- list(map(int,input().split())

- set(list(a)

- for i, j in zip(survey, choices):

- 입력 빠르게 받기
  ```python
  import sys
  input = sys.stdin.readline()
  ```

- dequq 스택과 큐의 기능을 한 번에
- 로또 파싱하기 
  - `replace("(","").replace(")","")` 가 핵심
  ```python
  data = [
      "1 2 3 4 5 (6)",
      "1 3 4 2 5 (7)"
  ]
  
  lotto_numbers = []
  for line in data:
      # 괄호 제거 후 분할
      parts = line.replace("(", "").replace(")", "").split()
      numbers = list(map(int, parts[:5]))
      bonus = int(parts[5])
      lotto_numbers.append((numbers, bonus))
  
  print(lotto_numbers)
  ```

- str() int() 타입 변환 확실하게
- 딕셔너리
   ``` python
   d = dict()
   d[a] = c

   sorted_dict = sorted(n.items(), key= lambda item:item[1], reverse=True) //딕셔너리 값으로 정렬
   ```
- 피보나치 수열
  ```python
  def solution(n):
    dp=[0,1] + [0]*n

    
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
  ```
- sep="", end=""
## SQL
- `DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE`
