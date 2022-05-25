from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

m, n = map(int ,stdin.readline().split())
graph = []
visit_graph = [[-1 for _ in range(n)] for _ in range(m)]
position = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for _ in range(m):
    graph.append(list(map(int, stdin.readline().split())))

def dfs(x, y):
    if [x, y] == [m -1, n - 1]:
        return 1
    
    if visit_graph[x][y] != -1:
        return visit_graph[x][y]
    
    visit_graph[x][y] = 0

    for p_x, p_y in position:
        n_x = x + p_x
        n_y = y + p_y

        if 0 <= n_x < m and 0 <= n_y < n:
            if graph[n_x][n_y] < graph[x][y]:
                visit_graph[x][y] += dfs(n_x, n_y)

    return visit_graph[x][y]

print(dfs(0, 0))
