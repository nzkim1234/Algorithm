from sys import stdin

n = 19
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
 
dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]    
 
def result():
    for x in range(n):
        for y in range(n):
            if graph[x][y]:

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1

                    # 가로, 새로, 우하향, 우상향 방향으로 올라가면서 오목인지 찾기
                    while 0 <= nx < n and 0 <= ny < n and graph[x][y] == graph[nx][ny]:
                        cnt += 1
 
                        if cnt == 5:
                            if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n and graph[nx][ny] == graph[nx + dx[i]][ny + dy[i]]:
                                break
                            if 0 <= x - dx[i] < n and 0 <= y - dy[i] < n and graph[x][y] == graph[x - dx[i]][y - dy[i]]:
                                break
                            return graph[x][y], x+1, y+1
 
                        nx += dx[i]
                        ny += dy[i]
    return 0, -1, -1
 
num, x, y = result()

print(num)

if num != 0:
    print(x, y)
