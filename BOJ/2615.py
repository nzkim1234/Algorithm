from sys import stdin

n = 19
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
 
dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]    
 
def result():
    for x in range(n):
        for y in range(n):
            if arr[x][y]:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1

                    while 0 <= nx < n and 0 <= ny < n and arr[x][y] == arr[nx][ny]:
                        cnt += 1
 
                        if cnt == 5:
                            if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < n and arr[nx][ny] == arr[nx + dx[i]][ny + dy[i]]:    # 육목 판정 1
                                break
                            if 0 <= x - dx[i] < n and 0 <= y - dy[i] < n and arr[x][y] == arr[x - dx[i]][y - dy[i]]:    # 육목 판정 2
                                break
                            return arr[x][y], x+1, y+1
 
                        nx += dx[i]
                        ny += dy[i]
    return 0, -1, -1
 
num, x, y = result()

print(num)

if num != 0:
    print(x, y)

