from sys import stdin

tc = int(stdin.readline())

for _ in range(tc):
    n, m, w = map(int, stdin.readline().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        s, e, t = map(int, stdin.readline().split())
        graph[s].append([e, t])
        graph[e].append([s, t])

    for _ in range(w):
        s, e, t = map(int,stdin.readline().split())
        graph[s].append([e, -t])

    result = False
    visit_graph = [1e9] * (n + 1)
    visit_graph[1] = 0
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for node, value in graph[j]:
                if visit_graph[node] > visit_graph[j] + value:
                    visit_graph[node] = visit_graph[j] + value
                    if i == n:
                        result = True
    
    if not result:
        print('NO')
    else:
        print('YES')