from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)

def dfs(current):
    global result
    visit_node.append(current)
    num = graph[current]

    if visit[num]:
        if num in visit_node:  # 방문노드에 이미 포함되어있으면 결과에 추가 == 하나의 사이클이 완성된다.
            result += visit_node[visit_node.index(num):]  # num부터의 인덱스가 사이클을 이룬다.
    else:
        visit[num] = True
        dfs(num)


t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    graph = [0] + list(map(int, stdin.readline().split()))
    visit = [False] * (n + 1)
    result = []

    for i in range(n + 1):
        if not visit[i]:
            visit_node = []  # dfs를 하면서 방문하는 노드들을 저장해둘 리스트
            visit[i] = True
            dfs(i)

    print(len(graph) - len(result))
