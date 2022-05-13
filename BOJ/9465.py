from sys import stdin

t = int(stdin.readline())

for i in range(t):
  graph = []
  n = int(stdin.readline())

    # 새로운 입력 추가
  for k in range(2):
    graph.append(list(map(int, stdin.readline().split())))
  
  for j in range(1, n):
    if j == 1:  # 첫번째 열은 왼쪽 대각선만 더해줌
      graph[0][j] += graph[1][j - 1]
      graph[1][j] += graph[0][j - 1]
    else:  # 왼쪽 대각선 또는 왼쪽 대각선의 왼쪽 인덱스 중 큰 값 더해줌
      graph[0][j] += max(graph[1][j - 1], graph[1][j - 2])
      graph[1][j] += max(graph[0][j - 1], graph[0][j - 2])
  
  print(max(graph[0][n - 1], graph[1][n - 1]))
