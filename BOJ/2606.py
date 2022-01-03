def dfs(v):
    check[v] = 1
    for i in graph[v]:
        if check[i] != 1:
            dfs(i)


def bfs(v):
    queue = []
    queue.append(v)
    while queue:
        x = queue.pop(0)
        if check != 1:
            check[x] = 1
            for i in graph[x]:
                if check[i] != 1:
                    queue.append(i)


c = int(input())
p = int(input())
graph = [[0] for _ in range(c+1)]
for i in range(p):
    x, y = map(int, input().split(' '))
    graph[x].append(y)
    graph[y].append(x)
for i in range(c+1):
    graph[i].sort()
check = [0] * (c+1)
check[0] = 1
bfs(1)  # or dfs(1)
print(check.count(1) - 2)
