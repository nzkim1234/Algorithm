from sys import stdin

n = int(stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(map(int, map(str, stdin.readline().strip()))))

def dfs(x, y, n):
    start_value = graph[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if start_value != graph[i][j]:
                n = n // 2

                print('(', end = '')
                
                dfs(x, y, n)
                dfs(x, y + n, n)
                dfs(x + n, y, n)
                dfs(x + n, y + n, n)
                
                print(')', end = '')
                
                return

    if start_value == 0:
        print('0', end = '')
    else:
        print('1', end = '')

dfs(0, 0, n)
