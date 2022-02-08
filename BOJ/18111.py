#PyPy3

from sys import stdin

n, m, b = map(int, stdin.readline().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))

min_height = min(map(min, graph))  # 최소 높이
max_height = max(map(max, graph))  # 최대 높이
leastTime = 1e9

for i in range(min_height, max_height + 1):
    pluscnt = 0
    minuscnt = 0

    for j in range(n):
        for k in range(m):
            h = graph[j][k] - i  

            # 높이차이가 양수, 음수 일때
            if h > 0:
                minuscnt += h
            elif h < 0:
                pluscnt -= h

    # 블록의 갯수가 부족하지 않을 때
    if minuscnt + b >= pluscnt:
        time = minuscnt * 2 + pluscnt

        if leastTime >= time:
            leastTime = time
            resultHeight = i

print(leastTime, resultHeight)
