from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())

graph = [[] for _ in range(h)]
loc_tomato = []  # 익은 토마토 위치 저장
count_0 = 0  # 안익은 토마토 갯수

for i in range(h):
    for j in range(n):
        indexs = list(map(int, stdin.readline().split()))
        
        for k in range(m):
            if indexs[k] == 1:
                loc_tomato.append([i, j, k])  # 익은 토마토의 위치 저장
            if indexs[k] == 0: 
                count_0 += 1  # 안익은 토마토의 갯수 증가
        
        graph[i].append(indexs)  # 그래프에 추가

time = 0
queue = deque(loc_tomato)
queue.append([-1, -1, -1])  # 한 사이클의 마지막 표시
position = [[0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]  # 익은 토마토의 인접 위치

while queue:
    s_h, s_x, s_y = queue.popleft()

    # 한 사이클의 끝이 났을 때
    if s_h + s_x + s_y < 0:
        # 큐가 남아있으면 다시 사이클의 끝을 표시, time += 1
        if queue:
            time += 1
            queue.append([-1, -1, -1])
    
    # bfs탐색
    for p_h, p_x, p_y in position:
        n_h, n_x, n_y = s_h + p_h, s_x + p_x, s_y + p_y
        
        if (0 <= n_h < h) and (0 <= n_x < n) and (0 <= n_y < m):
            if graph[n_h][n_x][n_y] == 0:
                count_0 -= 1  # 안익은 토마토의 갯수 감소
                graph[n_h][n_x][n_y] = 1  # 익은 토마토 표시
                queue.append([n_h, n_x, n_y])  # 큐에 추가

if count_0:  # 안 익은 토마토가 있을시 -1 출력
    print(-1)
else:  # 없을 시 time 출력
    print(time)
