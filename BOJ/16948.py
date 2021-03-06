from sys import stdin
from collections import deque

n = int(stdin.readline())
r1, c1, r2, c2 = map(int ,stdin.readline().split())
queue = deque([[r1, c1], [-1, -1]])
board = [[1e9 for _ in range(n)] for _ in range(n)]
position = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]
board[r1][c1] = 0
count = 1

while queue:
    r, c = queue.popleft()

    # 한 순환의 끝이면
    if r == -1 and c == -1:
        if queue:
            queue.append([-1, -1])
            count += 1
        continue
    
    # 이동가능한 범위 탐색
    for p_x, p_y in position:
        n_r = r + p_x
        n_c = c + p_y

        if 0 <= n_r < n and 0 <= n_c < n:
            if board[n_r][n_c] > count:
                board[n_r][n_c] = count
                queue.append([n_r, n_c])

if board[r2][c2] == 1e9:
     print(-1)
else:
    print(board[r2][c2])
