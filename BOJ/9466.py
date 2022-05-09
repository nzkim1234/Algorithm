from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)

def dfs(current):
    global result
    visit[current] = True
    visit_node.append(current)
    num = graph[current]

    if visit[num]:
        if num in visit_node:
            result += visit_node[visit_node.index(num):]
    else:
        dfs(num)


t = int(input())

for _ in range(t):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    visit = [False] * (n + 1)
    result = []

    for i in range(n + 1):
        if not visit[i]:
            visit_node = []
            dfs(i)

    print(len(graph) - len(result))