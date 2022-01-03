from collections import deque


def dfs(v):
    c1[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if c1[i] == 0:
            dfs(i)


def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        x = queue.popleft()
        if c2[x] == 0:
            print(x, end=' ')
            c2[x] = 1
            for i in graph[x]:
                if c2[i] == 0:
                    queue.append(i)


n, m, v = map(int, input().split(' '))
graph = [[0] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

c1 = [0] * (n+1)
c1[0] = 1
c2 = [0] * (n+1)
c2[0] = 1
dfs(v)
print()
bfs(v)
