from sys import stdin

n, start, end, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    s, e, v = map(int, stdin.readline().split())
    graph[s].append([e, v])

plus_value = list(map(int, stdin.readline().split()))

visit_graph = [-1e9] * n
visit_graph[start] = plus_value[start]
result = False
for i in range(n):
    for j in range(len(graph[i])):
        for k in range(n):
            if graph[i][j][0] == k:
                graph[i][j][1] = plus_value[k] - graph[i][j][1]

for i in range(n + 1):
    current = visit_graph[end]
    if current == -1e9 and i == n:
        print('gg')
        quit()
    for j in range(n):
        if visit_graph[j] == -1e9:
            continue
        for node, value in graph[j]:
            if visit_graph[j] != -1e9 and visit_graph[node] < visit_graph[j] + value + plus_value[node]:
                visit_graph[node] = visit_graph[j] + value + plus_value[node]
                if i == n:
                    check = [0] * n
                    queue = [node]
                    while queue:
                        current_node = queue.pop()
                        if current_node == end:
                            print('Gee')
                            quit()
                        check[current_node] = 1
                        for next_node, value in graph[current_node]:
                            if check[next_node] == 0:
                                queue.append(next_node)



print(visit_graph[end])

