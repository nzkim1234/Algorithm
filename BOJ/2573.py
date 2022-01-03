# pypy3

from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

position = [[0,1],[1,0],[-1,0],[0,-1]]
result = 0
visit_graph = [[False for _ in range(m)] for _ in range(n)]  # 빙산이 들렸는지 확인하는 리스트

while True:
    queue = deque()
    count_iceberg = 0
    island = 0
    count_sea = []

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:  # np_graph의 값이 0(바다)가 아닐시 visit_graph의 같은 좌표를 True로 변경
                visit_graph[i][j] = True
                count_iceberg += 1  # 빙산의 갯수 증가

    if count_iceberg <= 1:  # 빙산의 갯수가 1개보다 작거나 같을시 빙산이 갈라지지 않고 녹았다는 뜻이므로 reuslt = 0
        result = 0
        break

    # bfs 돌면서 island의 값, count의 값을 구한다
    for i in range(n):
        for j in range(m):
            if visit_graph[i][j] == True:
                queue.append([i,j])
                visit_graph[i][j] = False
                
                while queue:
                    count = 0
                    y, x = queue.pop()
                    for p_y, p_x in position:
                        n_y = y + p_y
                        n_x = x + p_x
                        if visit_graph[n_y][n_x] == True:
                            visit_graph[n_y][n_x] = False
                            queue.append([n_y, n_x])
                        if graph[n_y][n_x] == 0:
                            count += 1
                    count_sea.append([y, x, count])

                island += 1

    if island > 1:  # island가 2개 이상이면 빙산이 갈라졌으니 break
        break

    # count_sea에서 값을 참조하여 빙산 녹이기
    for y, x, s in count_sea: 
        if graph[y][x] - s < 0:
            graph[y][x] = 0
        else:
            graph[y][x] -= s

    result += 1

print(result)
