from sys import stdin
import heapq

n = int(stdin.readline())

graph = []

for _ in range(n):
    graph.append(list(map(int,map(str,stdin.readline().strip()))))

visit_graph = [[1e9 for _ in range(n)] for _ in range(n)]
queue = []
heapq.heappush(queue, [0, 0])
visit_graph[0][0] = 0

position = [[0, -1], [0, 1], [1, 0], [-1, 0]]

# 다익스트라 탐색
while queue:
    x, y = heapq.heappop(queue)

    for p_x, p_y in position:
        c_x = p_x + x
        c_y = p_y + y

        if 0 <= c_x < n and 0 <= c_y < n:

            # 흰색이면 벽을 부수지 않는다 visit_graph의 값 증가 x
            if graph[c_x][c_y] == 1 and visit_graph[c_x][c_y] > visit_graph[x][y]:
                visit_graph[c_x][c_y] = visit_graph[x][y]
                heapq.heappush(queue,[c_x, c_y])

            # 검은색이면 벽을 부순다. visit_graph의 값 증가 
            if graph[c_x][c_y] == 0 and visit_graph[c_x][c_y] > visit_graph[x][y] + 1:
                visit_graph[c_x][c_y] = visit_graph[x][y] + 1
                heapq.heappush(queue, [c_x, c_y])

print(visit_graph[n - 1][n - 1])
