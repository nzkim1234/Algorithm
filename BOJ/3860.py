from sys import stdin

while True:
    w, h = map(int,stdin.readline().split())
    
    if w == 0 and h == 0:
        break
    
    hole_graph = [[0 for _ in range(h)]for _ in range(w)]
    hole = [0]
    g = int(stdin.readline())

    for _ in range(g):
        x, y = map(int, stdin.readline().split())
        hole_graph[x][y] = -1
    
    e = int(stdin.readline())
    
    for i in range(1,e+1):
        in_x, in_y, out_x, out_y, value = map(int,stdin.readline().split())    
        hole_graph[in_x][in_y] = i
        hole.append([out_x, out_y, value])

    graph = [[float('inf') for _ in range(h)] for _ in range(w)]
    graph[0][0] = 0
    position = [[0,1], [1, 0], [0,-1], [-1, 0]]
    
    
    def dfs():
        for count in range(h * w):
            for x in range(w):
                for y in range(h):
                    if x == w - 1 and y == h - 1 or hole_graph[x][y] == -1:
                        continue
                    
                    if hole_graph[x][y] >= 1:
                        out_x, out_y, value = hole[hole_graph[x][y]]

                        if graph[out_x][out_y] > graph[x][y] + value :
                            graph[out_x][out_y] = graph[x][y] + value 

                            if count == h * w - 1 :
                                return float('-inf')

                    else:
                        for p_x,p_y in position:
                            n_x = x + p_x
                            n_y = y + p_y

                            if 0<= n_x <w and 0<= n_y <h : 
                                if hole_graph[n_x][n_y] >=0 :
                                    if graph[n_x][n_y] > graph[x][y] + 1:
                                        graph[n_x][n_y] = graph[x][y] + 1
                                        
                                        if count == h * w - 1:
                                            return float('-inf')
                                   
        return graph[w - 1][h - 1]
    

    result = dfs()

    if result == float('-inf') :
        print('Never')
    else:
        if result == float('inf'):
            print('Impossible')
        
        else:
            print(result)              
