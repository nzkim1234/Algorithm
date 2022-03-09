from sys import stdin

n, m = map(int, stdin.readline().split())
result = []

def dfs(index):
    if len(result) == m:
        print(*result) 
        return

    for i in range(index, n + 1):
        if not i in result:
            result.append(i)
            dfs(i + 1)
            result.pop()

dfs(1)