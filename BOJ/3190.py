from sys import stdin
from collections import deque

n = int(stdin.readline())
graph = [[0 for _ in range(n)] for _ in range(n)]
graph[0][0] = 1
movement = deque()
time = 0
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
direction_index = 0
snake_head = [0, 0]
snake_body = deque()


for k in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    graph[x-1][y-1] = 2


for l in range(int(stdin.readline())):
    switch_time, rotate = stdin.readline().split()
    movement.append([int(switch_time), rotate])

switch_time, rotate = movement.popleft()  # 방향이 바뀌는 시간, 바뀌는 방향 저장

while True:
    if switch_time == time:
        #  rortate 값에 따라 진행 방향을 바꾼다.
        if rotate == 'D':
            direction_index += 1
            
            if direction_index > 3:
                direction_index = 0
        else:
            direction_index -= 1
            
            if direction_index < 0:
                direction_index = 3
        
        if movement:  # 덱이 남아있을 시 switch_time, rotate 값을 변경
            switch_time, rotate = movement.popleft()

    n_x = snake_head[0] + direction[direction_index][0]  # 새로운 뱀 머리의 x좌표
    n_y = snake_head[1] + direction[direction_index][1]  # 새로운 뱀 머리의 y좌표

    if 0 <= n_x < n and 0 <= n_y < n and graph[n_x][n_y] != 1:  # 새로운 뱀의 좌표가 그래프 내부이며 값이 1(뱀의 몸통) 이 아닐 때
        snake_body.append(snake_head)  # 이전 뱀 머리의 좌표를 몸통에 저장
        snake_head = [n_x, n_y]  # 새로운 뱀 머리의 좌표를 주장

        if graph[n_x][n_y] != 2:  # 새로운 뱀 머리의 좌표값이 2가 아니면
            r_x, r_y = snake_body.popleft()  # 뱀 몸통의 마지막을 삭제
            graph[r_x][r_y] = 0  # 마지막 뱀 몸통의 값을 0 으로 변경

        graph[n_x][n_y] = 1  # 새로운 뱀 머리의 좌표값을 1로 변경
    else:
        break

    time += 1

print(time + 1)