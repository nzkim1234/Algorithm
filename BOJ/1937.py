from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

n = int(stdin.readline())
graph = []
position = [[-1, 0], [0, -1], [1, 0], [0, 1]]
result = 0
result_graph = [[0] * n for _ in range(n)]


def dfs(c_x, c_y):

    for i in result_graph:
        print(i)
    print()
    if result_graph[c_x][c_y]:
        return result_graph[c_x][c_y]

    result_graph[c_x][c_y] = 1

    for p_x, p_y in position:
        n_x, n_y = c_x + p_x, c_y + p_y

        if 0 <= n_x < n and 0 <= n_y < n:  
            if graph[n_x][n_y] > graph[c_x][c_y]:
                result_graph[c_x][c_y] = max(result_graph[c_x][c_y], dfs(n_x, n_y) + 1)
    
    return result_graph[c_x][c_y]


for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

for x in range(n):
    for y in range(n):
        result = max(result, dfs(x, y))

print(result)