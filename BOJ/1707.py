from sys import stdin

k = int(stdin.readline())

for _ in range(k):
    v, e = map(int, stdin.readline().split())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        u, v = map(int ,stdin.readline().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    print(graph)
