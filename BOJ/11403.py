from sys import stdin

n = int(stdin.readline())
graph = []

for i in range(n):
    graph.append(list(map(int, stdin.readline().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in graph:
    print(*i)
