from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = []
shark_size = shark_grow = 2
shark_loc = []
result = 0
queue = deque()
position = [[-1, 0], [0, -1], [1, 0], [0, 1]]

for i in range(n):
    l = list(map(int, stdin.readline().split()))
    graph.append(l)

    if 9 in l:  # 상어의 첫 위치 찾기
        shark_loc = [i, l.index(9)]

while True:
    queue.append([shark_loc[0], shark_loc[1], 1])  # 큐에다가 상어의 좌표, 움직인 거리를 저장
    visit_graph = [[False for _ in range(n)] for _ in range(n)]
    eatable_fish = []

    # bfs 탐색
    while queue:
        x, y, distance = queue.popleft()
        visit_graph[x][y] = True
        for p_x, p_y in position:
            n_x = x + p_x
            n_y = y + p_y

            if 0 <= n_x < n and 0 <= n_y < n and not visit_graph[n_x][n_y]:
                if 0 < graph[n_x][n_y] < shark_size:  # 먹을 수 있는 크기의 물고기면
                    eatable_fish.append([n_x, n_y, distance])  # 좌표값과 움직인 거리를 eatable_fish에 저장
                elif graph[n_x][n_y] == 0 or graph[n_x][n_y] == shark_size:  # 칸이 비어있거나, 칸의 물고기 크기가 상어의 크기와 같다면
                    queue.append([n_x, n_y, distance + 1])  # 큐에 좌표값과 움직인 거리를 저장
                    visit_graph[n_x][n_y] = True
    
    if not eatable_fish:  # eatable_fish가 비어있으면 종료
        break
    else:
        eatable_fish.sort(key = lambda x : (x[2], x[0], x[1]))  # 리스트를 움직인 거리, x좌표, y좌표 순으로 정렬
        graph[shark_loc[0]][shark_loc[1]] = 0  # 기존 상어의 위치를 빈칸으로 바꾸기
        shark_loc = [eatable_fish[0][0], eatable_fish[0][1]]  # 물고기를 먹은 위치를 새로운 상어 위치로 저장
        graph[shark_loc[0]][shark_loc[1]] = 9  # 바뀐 상어의 위치를 9(상어)로 바꾸기
        shark_grow -= 1  # 상어가 성장하기까지 필요한 물고기 수 -1
        
        if shark_grow == 0:  # 상어가 성장가능하다면 성장하기
            shark_size = shark_grow = shark_size + 1

        result += eatable_fish[0][2]  # 상어가 이동한 거리를 결과에 저장

print(result)
