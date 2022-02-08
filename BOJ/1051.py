from sys import stdin

n, m = map(int, stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, map(str, stdin.readline().strip()))))

result = 1

for row in range(n):
    for col in range(m):
        length = 0
        
        if graph[row].count(graph[row][col]) > 1:

            for col2 in range(col, m):
                if graph[row][col2] == graph[row][col]:
                    length = col2 - col

                    if 0 <= row + length < n:
                        if graph[row + length][col] == graph[row][col] and graph[row + length][col2] == graph[row][col]:
                            result = max(result, (length + 1) * (length + 1))

print(result)
