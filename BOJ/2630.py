from sys import stdin

n = int(stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(map(int,stdin.readline().split())))

count_w = 0
count_b = 0


def dfs(x, y, n):
    start_value = graph[x][y]
    global count_b
    global count_w

    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != start_value:
                n = n // 2

                dfs(x, y, n)
                dfs(x, y + n, n)
                dfs(x + n, y , n)
                dfs(x +n, y + n, n)
                
                return

    if start_value == 1:
        count_b += 1
    else:
        count_w += 1


dfs(0, 0, n)

print(count_w)
print(count_b)