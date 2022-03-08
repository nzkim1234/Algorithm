from sys import stdin

n = int(stdin.readline())
graph = [0] * (n + 1)
result = []

for i in range(1, n + 1):
    graph[i] = int(stdin.readline())

# dfs 탐색, new_index = 다음 인덱스, index = 처음 인덱스
def dfs(new_index, index):
    visit_graph[new_index] = True

    if not visit_graph[graph[new_index]]:
        dfs(graph[new_index], index)
    elif visit_graph[graph[new_index]] and graph[new_index] == index:
        result.append(graph[new_index])


for i in range(1, n + 1):
    visit_graph = [False] * (n + 1)
    dfs(i, i)

print(len(result))

for r in result:
    print(r)
