from sys import stdin

while True:    
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break
    graph = [[0 for _ in range(w)] for _ in range(h)]
    g = int(stdin.readline())
    for _ in range(g):
        x, y = map(int,stdin.readline().split())
        graph[y][x] = 1
    e = int(stdin.readline())
    hole = []
    for _ in range(e):
        hole.append(list(map(int,stdin.readline().split())))

    for i in graph:
        print(i)
    print(hole)