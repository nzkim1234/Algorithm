from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    graph = sorted(list(map(int, stdin.readline().split())), reverse=True)
    result = 0
    for i in range(n-2):
        result = max(result, graph[i] - graph[i + 2])
    print(result)
