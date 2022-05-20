from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = []
visit_graph = [[False for _ in range(n)] for _ in range(n)]  # 방문 여부
position = [[0, 1], [1, 0], [-1, 0], [0, -1]]  # 움직일 수 있는 방향 표시
num = 1  # 섬어 붙일 번호
answer = 1e9  # 답

# 그래프 입력받기
for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

# bfs를 돌면서 섬의 위치를 파악 하나의 섬에 통일된 번호(num) 부여
for x in range(n):
    for y in range(n):
        if not visit_graph[x][y]and graph[x][y] == 1:
            num += 1
            queue = deque()
            queue.append([x, y])
            visit_graph[x][y] = True
            graph[x][y] = num

            while queue:
                c_x, c_y = queue.popleft()

                for p_x, p_y in position:
                    n_x = p_x + c_x
                    n_y = p_y + c_y

                    if 0 <= n_x < n and 0 <= n_y < n:
                        if not visit_graph[n_x][n_y]  and graph[n_x][n_y] == 1:
                            visit_graph[n_x][n_y] = True
                            graph[n_x][n_y] = num
                            queue.append([n_x, n_y])

visit_graph = [[1e9 for _ in range(n)] for _ in range(n)]  # 방문 그래프를 다시 초기화, 좌표까지의 거리를 저장

# bfs탐색을 하면서 다른 섬 까지의 최솟값 찾기
for x in range(n):
    for y in range(n):
        if graph[x][y] != 0:
            num = graph[x][y]
            queue = deque()
            queue.append([x,y])
            queue.append([-1, -1])  # 하나의 사이클의 끝을 나타냄
            distance = 1  # 거리를 표현

            while queue:
                c_x, c_y = queue.popleft()

                # 하나의 사이클이 끝나면 다시 -1-1로 사이클의 끝을 표현하고 거리값을 늘림
                if [c_x, c_y] == [-1, -1]:
                    if queue:
                        distance +=1 
                        queue.append([-1, -1])
                    continue

                for p_x, p_y in position:
                    n_x = c_x + p_x
                    n_y = c_y + p_y
                    
                    if 0 <= n_x < n and 0 <= n_y < n and  graph[n_x][n_y] != num:  # 그래프 내부, 같은 섬이 아닐 때
                        if visit_graph[n_x][n_y] > distance:  # 거리가 더 가까울 때
                            if graph[n_x][n_y] == 0:  # 바다일 경우
                                visit_graph[n_x][n_y] = distance
                                queue.append([n_x, n_y])
                            elif graph[n_x][n_y] != num:  # 다른 섬일 경우
                                answer = min(distance - 1, answer)

print(answer )