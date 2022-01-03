# RecursionError 방지용
import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):
    if i >= 0 and i < h and j >= 0 and j < w:
        if graph[i][j] == 1:
            graph[i][j] = 0
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j+1)
            dfs(i+1, j)
            dfs(i+1, j-1)
            dfs(i-1, j+1)
            dfs(i-1, j)
            dfs(i-1, j-1)


def bfs(i, j):
    queue = []
    queue.append((i, j))
    while queue:
        x, y = queue.pop(0)
        if x >= 0 and x < h and y >= 0 and y < w:
            if graph[x][y] == 1:
                graph[x][y] = 0
                queue.append((x+1, y+1))
                queue.append((x+1, y))
                queue.append((x+1, y-1))
                queue.append((x-1, y+1))
                queue.append((x-1, y))
                queue.append((x-1, y-1))
                queue.append((x, y+1))
                queue.append((x, y-1))


while True:
    count = 0
    w, h = map(int, input().split())
    if w+h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                count += 1
                dfs(i, j)  # bfs(i, j)
    print(count)
