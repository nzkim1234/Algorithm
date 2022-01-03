from sys import stdin
from collections import deque
INF = int(1e9)

direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 이동가능한 방향
count = 0

while True:
    count += 1
    n = int(stdin.readline())
    
    if not n:  # n이 0일시 break
        break

    queue = deque()
    graph = []  # 원본 그래프
    d_graph = [[INF for _ in range(n)] for _ in range(n)]  # 거리 값이 저장될 그래프

    for _ in range(n):
        graph.append(list(map(int, stdin.readline().split())))
    
    d_graph[0][0] = graph[0][0] 
    queue.append([0, 0])

    while queue:
        x, y = queue.popleft()

        # 이동가능한 방향을 보고 이동해 온 거리값 + 칸의 거리값 < 칸에 저장되어있는 값 일시 칸의 거리값을 최소인 값으로 바꾸기
        for p_x, p_y in direction:
            n_x = x + p_x
            n_y = y + p_y
            
            if 0 <= n_x < n and 0 <= n_y < n:
                if graph[n_x][n_y] + d_graph[x][y] < d_graph[n_x][n_y]:
                    d_graph[n_x][n_y] = graph[n_x][n_y] + d_graph[x][y]
                    queue.append([n_x, n_y])
 
    print("Problem " + str(count) + ": " + str(d_graph[n-1][n-1]))