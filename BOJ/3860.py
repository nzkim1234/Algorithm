from sys import stdin

while True:    
    w, h = map(int, stdin.readline().split())

    if w == 0 and h == 0:
        break

    graph = [[1e9 for _ in range(w)] for _ in range(h)]
    g = int(stdin.readline())

    for _ in range(g):
        x, y = map(int,stdin.readline().split())
        graph[y][x] = 'hole'

    e = int(stdin.readline())
    hole = dict()

    for _ in range(e):
        in_x, in_y, out_x, out_y, value = map(int, stdin.readline().split())
        hole[str(in_y) + ',' + str(in_x)] = [out_y, out_x, value]

    position = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    graph[0][0] = 0


    def calc():
        for i in range(w * h):
            for y in range(h):
                for x in range(w):
                    if x == w - 1 and y == h - 1 or graph[y][x] == 'hole':
                        continue
                    
                    if str(y) + ',' + str(x) in hole.keys():
                        hole_y, hole_x, value = hole[str(y) + ',' + str(x)]

                        if graph[hole_y][hole_x] > graph[y][x] + value:
                            graph[hole_y][hole_x] = graph[y][x] + value

                            if i == h * w - 1:
                                return False
                    
                    else:
                        for p_y, p_x in position:
                            n_y = y + p_y
                            n_x = x + p_x
                            
                            if 0 <= n_y < h and 0 <= n_x < w and graph[n_y][n_x] != 'hole':
                                if graph[n_y][n_x] > graph[y][x] + 1:
                                    graph[n_y][n_x] = graph[y][x] + 1
                                    
                                    if i == h * w - 1:
                                        return False
        return graph[h - 1][w - 1]

    answer = calc()

    if not answer:
        print('Never')
    else:
        if answer == 1e9:
            print('Impossible')
        else:
            print(answer)