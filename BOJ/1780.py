from sys import stdin

n = int(stdin.readline())
minus_paper, zero_paper, plus_paper = 0, 0, 0
graph = []

for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))


def dfs(x, y, n):
    global minus_paper
    global zero_paper
    global plus_paper
    current_num = graph[x][y]

    for c_x in range(x, x + n):
        for c_y in range(y, y + n):
            if graph[c_x][c_y] != current_num:  # 다른 숫자가 있을 경우
                
                # 9등분 하기
                for n_x in range(3):
                    for n_y in range(3):
                        dfs(x + (n_x * n // 3), y + (n_y * n // 3), n//3)
                
                return 
    
    if current_num == -1:
        minus_paper += 1
    elif current_num == 0:
        zero_paper += 1
    else:
        plus_paper += 1


dfs(0, 0, n)

print(minus_paper)
print(zero_paper)
print(plus_paper)
