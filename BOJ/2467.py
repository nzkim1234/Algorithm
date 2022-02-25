from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    graph = []
    is_sorted = True

    for _ in range(n):
        graph.append(stdin.readline().strip())

    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if graph[j] in graph[i]:
                is_sorted = False
                break
        if not is_sorted:
            break
    if is_sorted:
        print('YES')
    else:
        print('NO')