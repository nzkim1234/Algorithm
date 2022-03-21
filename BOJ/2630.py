from sys import stdin

n = int(stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(map(int,stdin.readline().split())))

count_w = 0
count_b = 0


def dfs(x, y, n):
    start_value = graph[x][y]
    global count_b  # 전역변수로 사용
    global count_w  # 전역변수로 사용

    # 범위를 돌면서 숫자가 start_value랑 다를시 범위를 좁힘(dfs 탐색)
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != start_value:
                n = n // 2

                dfs(x, y, n)  # 1사분면
                dfs(x, y + n, n)  # 2사분면
                dfs(x + n, y , n)  # 3사분면
                dfs(x +n, y + n, n)  # 4사분면
                
                return

    # 모든 범위가 같은 숫자일경우 그 숫자에 맞는 값 증가
    if start_value == 1:
        count_b += 1
    else:
        count_w += 1


dfs(0, 0, n)

print(count_w)
print(count_b)
