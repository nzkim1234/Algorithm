from collections import deque

position = [[1,0], [0,1], [-1,0], [0,-1]]

def bfs():
    c = 0
    while p_player:
        c += 1
        while p_fire:
                if p_fire[0][2] < c:
                    p_y, p_x, time = p_fire.popleft()
                    for y, x in position:
                        new_y = y + p_y
                        new_x = x + p_x
                        if 0 <= new_x < w and 0 <= new_y < h:
                            if graph[new_y][new_x] == '.' or graph[new_y][new_x] == '@':
                                graph[new_y][new_x] = '*'
                                p_fire.append([new_y, new_x, time + 1])
                else:
                    break
        while p_player:
            if p_player[0][2] < c:
                p_y, p_x, time = p_player.popleft()
                for y, x in position:
                    new_y = y + p_y
                    new_x = x + p_x
                    if 0 <= new_x < w and 0 <= new_y < h:
                        if graph[new_y][new_x] == "." and  visited[new_y][new_x] != 1:
                            visited[new_y][new_x] = 1
                            p_player.append((new_y, new_x, time + 1))
                    else:
                        return c
            else:
                break
    return "IMPOSSIBLE"

                            

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    graph = []
    visited = [[0 for _ in range(w)] for _ in range(h)]
    p_fire = deque()
    p_player = deque()
    for i in range(h):
        graph.append(list(input()))
        for j in range(w):
            if graph[i][j] == '@':
                visited[i][j] = 1
                p_player.append([i, j, 0])
            if graph[i][j] == '*':
                p_fire.append([i, j, 0])
    print(bfs())
    