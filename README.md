# 1일 1알고리즘
This is a auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).

# [문제 풀이 일지](https://hi-jin-1514.notion.site/2769b2ff4b1180018635f8c86d32c52d?v=2769b2ff4b1180e28d0c000cf0ed9e6b&source=copy_link)

# 오답노트

<details>
<summary> 파이썬 </summary>
  
- 입력 빠르게 받기
  ```python
  import sys
  input = sys.stdin.readline()
  ```
- sort
- ![img_1.png](https://wikidocs.net/images/page/232020/03-1-12.png)

  - l.sort()는 원본 자체를 정렬
  - l2 = l.sorted()는 원본 그대로 두고 정렬
  - 버블정렬은 N^2 / sort는 nlogn
  - set은 n

- `enumerate()`
  - 리스트 안에 있는걸 인덱스랑 같이 반환할 수 있음 
  - `for i, num in enumerate(nums):`
- for i, j in zip(survey, choices):
  - 두 리스트를 한번에 돌림

- list(map(int,input().split())

- set(list(a))
- s.split() 
  ```python 
  s = '10 20 Z 30'
  s = s.split() # s = ['10', '20', 'Z', '30']
  ```
- popleft()
  ```python
  from collections import deque
  a = deque()
  [a.append(i) for i in range(5)]
  a.pop() #deque([0, 1, 2, 3])

  
  b = deque()
  [b.append(i) for i in range(5)]
  b.popleft() #deque([1, 2, 3, 4])
  ```
- 배열에 있는 값이 큰순서대로 인덱스 출력하기
  ```python
  sorted_indexed_list = sorted(enumerate(per), key=lambda x: x[1], reverse=True)

  # 정렬된 결과에서 인덱스만 추출
  sorted_indices = [index + 1 for index, value in sorted_indexed_list]
  ```

- dequeue 스택과 큐의 기능을 한 번에
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
</details>

<details>
<summary> SQL </summary>
  
- `DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE`
</details>
