# RecursionError 방지용
import sys
sys.setrecursionlimit(10**6)


def dfs(x, y):
    if x >= 0 and x < m and y >= 0 and y < n:
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)


def bfs(x, y):
    queue = []
    queue.append([x, y])
    while queue:
        nx, ny = queue.pop(0)
        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx+1, ny])
                queue.append([nx-1, ny])
                queue.append([nx, ny+1])
                queue.append([nx, ny-1])


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split(' '))
    graph = []
    count = 0
    for i in range(m):
        graph.append(list())
        for j in range(n):
            graph[i].append(0)
    for _ in range(k):
        x, y = map(int, input().split(' '))
        graph[x][y] = 1
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                count += 1
                bfs(i, j)  # dfs(i, j)
    print(count)
