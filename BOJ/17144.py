#pypy3

from sys import stdin

r, c, t = map(int, stdin.readline().split())
graph = []
position = [[0, 1], [1, 0], [-1, 0], [0, -1]]
aircleaner = []

for row in range(r):
    graph.append([])
    
    for dust in list(map(int, stdin.readline().split())):
        graph[row].append([dust, 0])
        
        if dust == -1:
            aircleaner.append([row, graph[row].index([dust, 0])])

for _ in range(t):
    
    # 미세먼지 확산
    for i in range(r):
        for j in range(c):
            if graph[i][j][0] > 0:
                count = 0  # 확산되는 칸의 갯수를 알기 위한 변수

                # 인접한 칸에 확산이 가능하다면 확산
                for p_x, p_y in position:
                    n_x, n_y = i + p_x, j + p_y
                    
                    if 0 <= n_x < r and 0 <= n_y < c:
                        if graph[n_x][n_y][0] != -1:
                            count += 1
                            graph[n_x][n_y][1] += graph[i][j][0] // 5
                
                graph[i][j][0] = graph[i][j][0] - (graph[i][j][0] // 5 * count)  # 확산한 다음 남은 먼지의 양

    # 확산이 끝난뒤 칸의 미세먼지양 계산
    for i in range(r):
        for j in range(c):
            if graph[i][j][1] != 0:
                graph[i][j][0] += graph[i][j][1]
                graph[i][j][1] = 0

    # 위쪽 공기청정기의 동작
    rorate = 0  # 회전을 위한 변수
    air_x = aircleaner[0][0]  # 공기청정기의 x좌표
    air_y = aircleaner[0][1]  # 공기청정기의 y좌표
    storage = -1  # 이전 값을 저장하기 위한 변수

    # 반시계 방향으로 순환
    while True:
        if rorate == 0:  # 좌 -> 우
            if 0 <= air_y + 1 < c:
                air_y += 1
                new_storage = graph[air_x][air_y]

                if storage != -1:  # 시작점 다음 칸이 아니라면
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = [0, 0]
                    
                storage = new_storage
            else:
                rorate += 1

        elif rorate == 1:  # 하 -> 상
            if 0 <= air_x - 1 < r:
                air_x -= 1
                new_storage = graph[air_x][air_y]

                if storage != -1:  # 시작점 다음 칸이 아니라면
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = [0, 0]

                storage = new_storage
            else:
                rorate += 1

        elif rorate == 2:  # 우 -> 좌
            if 0 <= air_y - 1 < c:
                air_y -= 1
                new_storage = graph[air_x][air_y]
                
                if storage != -1:  # 시작점 다음 칸이 아니라면
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = [0, 0]

                storage = new_storage
            else:
                rorate += 1

        elif rorate == 3:  # 상 -> 하
            if 0 <= air_x + 1 < r:
                air_x += 1

                if [air_x, air_y] == aircleaner[0]:
                    break
                
                new_storage = graph[air_x][air_y]
                
                if storage != -1:  # 시작점 다음 칸이 아니라면
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = [0, 0]
                
                storage = new_storage
            else:
                break

    # 아래쪽 공기청정기의 동작
    rorate = 0  # 회전을 위한 변수
    air_x = aircleaner[1][0]  # 공기청정기의 x좌표
    air_y = aircleaner[1][1]  # 공기청정기의 y좌표
    storage = -1  # 이전 값을 저장하기 위한 변수

    while True:
        if rorate == 0:  # 좌 -> 우
            if 0 <= air_y + 1 < c:
                air_y += 1
                new_storage = graph[air_x][air_y]

                if storage != -1:  # 시작점 다음 칸이 아니라면
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = [0, 0]

                storage = new_storage
            else:
                rorate += 1

        elif rorate == 1:  # 상 -> 하
            if 0 <= air_x + 1 < r:
                air_x += 1
                new_storage = graph[air_x][air_y]

                if storage != -1:  # 시작점 다음 칸이 아니라면
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = [0, 0]

                storage = new_storage
            else:
                rorate += 1

        elif rorate == 2:  # 우 -> 좌
            if 0 <= air_y - 1 < c:
                air_y -= 1
                new_storage = graph[air_x][air_y]

                if storage != -1:  # 시작점 다음 칸이 아니라면
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = [0, 0]

                storage = new_storage
            else:
                rorate += 1

        elif rorate == 3:  # 하 -> 상
            if 0 <= air_x - 1 < r:
                air_x -= 1

                if [air_x, air_y] == aircleaner[1]:
                    break

                new_storage = graph[air_x][air_y]

                if storage != -1:  # 시작점 다음 칸이 아니라면
                    graph[air_x][air_y] = storage
                else:
                    graph[air_x][air_y] = [0, 0]

                storage = new_storage
            else:
                break

result = 0

for i in graph:
    for j in i:
        result += j[0]

print(result + 2)
