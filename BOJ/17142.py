from sys import stdin
from collections import deque
from itertools import combinations

n, m = map(int, stdin.readline().split())
virus_startpoints = []
graph = []
position = [[0, 1], [1, 0], [-1, 0], [0, -1]]
base_empty_space = 0

# 그래프를 입력받으면서 0인 자리 카운팅 , 비활 상태인 바이러스 자리 저장
for row in range(n):
    one_line = list(map(int, stdin.readline().split()))

    for col in range(n):
        if one_line[col] == 0:
            base_empty_space += 1
        elif one_line[col] == 2:
            virus_startpoints.append([row, col])
            one_line[col] = -1

    graph.append(one_line)

c_virus_startpoints = list(combinations(virus_startpoints, m))  # 바이러스를 활성화시킬 숫자로 조합 생성
case = 1
result = 1e9

for virus_startpoint in c_virus_startpoints:
    case += 1  # 
    virus_queue = deque(virus_startpoint)
    virus_queue.append([-1, -1])  # 시간의 증가를 위해서 추가
    empty_space = base_empty_space
    count = 0

    if empty_space <= 0:
        result = 0
        break

    count += 1

    # bfs 탐색
    while virus_queue:
        
        # 최솟값보다 크면 종료
        if count >= result:
            break

        x, y = virus_queue.popleft()
        
        # 빈칸이 없을 경우 종료
        if empty_space <= 0:
            break
        
        # 시간의 경과
        if [x, y] == [-1, -1]:
            count += 1

            # 더 처리할 데이터가 있다면
            if len(virus_queue) > 0:
                virus_queue.append([-1, -1])

            continue
        
        # 좌표값 방문처리
        if graph[x][y] != case:
            graph[x][y] = case
        
        # 상하좌우 돌면서 방문하지 않은 좌표면 방문 처리
        for p_x, p_y in position:
            n_x = x + p_x
            n_y = y + p_y

            if 0 <= n_x < n and 0 <= n_y < n:
                if graph[n_x][n_y] != 1:
                    if graph[n_x][n_y] != case:
                        graph[n_x][n_y] = case

                        # 빈칸이면 empty_space 감소
                        if not [n_x, n_y] in virus_startpoints:
                            empty_space -= 1

                        virus_queue.append([n_x, n_y])

    # 모든 빈칸을 다 방문했으면 결과값 갱신
    if empty_space <= 0:
        result = min(result, count)

if result == 1e9:
    print(-1)
else:
    print(result)
