from sys import stdin

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b, c])

visit_graph = [1e9] * (n + 1)
visit_graph[1] = 0
result = True

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for node, value in graph[j]:
            if visit_graph[j] != 1e9 and visit_graph[node] > visit_graph[j] + value:
                visit_graph[node] = visit_graph[j] + value
                if i == n:
                    result = False

if not result:
    print(-1)
else:
    for i in visit_graph[2::]:
        if i >= 1e9:
            print(-1)
        else:
            print(i)