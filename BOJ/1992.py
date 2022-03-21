from sys import stdin

n = int(stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(map(int, map(str, stdin.readline().strip()))))

def dfs(x, y, n):
    start_value = graph[x][y]  # 시작값

    # 구간을 탐색하면서 하나라도 값이 다르면 더 범위를 좁혀서 탐색(dfs)
    for i in range(x, x + n):
        for j in range(y, y + n):
            if start_value != graph[i][j]:
                n = n // 2

                print('(', end = '')
                
                dfs(x, y, n)  # 1사분면
                dfs(x, y + n, n)  # 2사분면
                dfs(x + n, y, n)  # 3사분연
                dfs(x + n, y + n, n)  # 4사분면
                
                print(')', end = '')
                
                return  
    
    # 모든 값이 같으면 그 값을 출력
    if start_value == 0:
        print('0', end = '')
    else:
        print('1', end = '')

dfs(0, 0, n)
