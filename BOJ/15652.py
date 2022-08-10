from sys import stdin

n, m = map(int, stdin.readline().split())
answer = []


def dfs(start, size):
    if size == m:
        print(*answer)
        return

    for i in range(start, n + 1):
        answer.append(i)
        dfs(i , size + 1)
        answer.pop()


for s in range(1, n + 1):
    answer = [s]
    dfs(s, 1)
