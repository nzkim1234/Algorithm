from collections import deque


def bfs():
    count = 0
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        count += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(len(d)):
                nx = x + d[i][0]
                ny = y + d[i][1]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        queue.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                print(-1)
                quit()
    count -= 1
    print(count)


m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
queue = deque(())
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
bfs()
