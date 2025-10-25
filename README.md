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
- popleft() = pop(0)
- ![img.png](https://velog.velcdn.com/images/snghyun331/post/ea7102a9-a733-4077-a695-89e8daa194e3/image.png)
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
- DFS 깊이우선탐색-재귀
  ```python
  graph = {
      1: [4,5],
      2: [3],
      3: [],
      4: [2,3],
      5: [4]
  }
  
  visited = [ False ] * (len(graph) +1)
  
  def dfs(current_node):
      visited[current_node] = True
      print(current_node)
  
      for i in graph[current_node]:
          if not visited[i]:
              dfs(i)
  
  dfs(1)
  ```
- BFS 너비우선탐색-큐
  ```python
  from collections import deque
  
  graph = {
      1: [4,5],
      2: [3],
      3: [],
      4: [2,3],
      5: [4]
  }
  
  
  def bfs(start_node):
      visited = [False] * (len(graph) +1)
  
      queue = deque([start_node])
      while queue:
          node = queue.popleft()
          print(node)
  
          for i in graph[node]:
              if not visited[i]:
                  queue.append(i)
                  visited[i] = True
  
  bfs(1)
  ```
- 유기농배추
  ```python
  #dfs
  import sys
  sys.setrecursionlimit(10000)
  from sys import stdin
  input = stdin.readline
  
  from collections import deque
  
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  
  t = int(input())
  for _ in range(t):
      m, n, k = map(int, input().split())
      graph = [[0 for _ in range(m)] for _ in range(n)]
  
      for _ in range(k):
          a, b = map(int, input().split())
          graph[b][a] = 1
  
      def dfs(x, y): #재귀
          graph[y][x] = 0  # 시작점 방문 처리
  
          for i in range(4):
              nx = x + dx[i]
              ny = y + dy[i]
  
              if nx < 0 or nx >= m or ny < 0 or ny >= n:
                  continue
  
              if graph[ny][nx] == 0:
                  continue
  
              if graph[ny][nx] == 1:
                  # graph[ny][nx] = 0  # 방문처리 안해도 됨
                  dfs(nx,ny)
  
      def bfs(x,y):
          queue = deque()
          queue.append((x,y))
          graph[y][x] = 0 #시작점 방문처리
  
          while queue:
              x,y = queue.popleft()
              for i in range(4):
                  nx = x + dx[i]
                  ny = y + dy[i]
  
                  if nx<0 or nx>=m or ny<0 or ny>=n:
                      continue
  
                  if graph[ny][nx]:
                      graph[ny][nx] = 0 #방문처리
                      queue.append((nx,ny))
  
  
  
      answer = 0
      for y in range(n):
          for x in range(m):
              if graph[y][x] == 1:
                  # dfs(x, y)
                  bfs(x,y)
                  answer += 1
      print(answer)
  ```
- 시뮬레이션
  ![img.png](https://img1.daumcdn.net/thumb/C163x110@2x.fwebp.q85/?fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FRRSJf%2FbtrFGzBltl1%2FAAAAAAAAAAAAAAAAAAAAAFIzCKaBISbmu-8ntUennPApvfrq6KItFMHJFPNw_5Mu%2Fimg.jpg%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1753973999%26allow_ip%3D%26allow_referer%3D%26signature%3DA9yHeoFnKRTjrkdCtMY0IS06Ebw%253D)
  ```
  (0,0)에서 시작. 좌측 상단
  
  move_type = ['L', 'R', 'U', 'D']
  dx = [0, 0, -1, 1]
  dy = [-1, 1, 0, 0]
  
  x,y =1,1
  data = list(input().split())
  
  for i in data:
      for t in range(len(move_type)):
          if i == move_type[t]:
              nx = x + dx[t] #초기화 안해도 파이썬은 가능
              ny = y + dy[t]
  
      if nx <1 or ny < 1 or nx >n or ny>n:
          continue
  
      x = nx
      y = ny
  ```
  - 알파벳 -> 숫자
    - 대문자 `ord(문자) - ord('A') + 1`
    - 소문자 `ord(문자) - ord('a') + 1`
</details>

<details>
<summary> SQL </summary>
  
- `DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') as PUBLISHED_DATE`
</details>
