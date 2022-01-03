def dfs(v):
    l = graph[v]
    graph[v] = -2
    if l != -2:
        for i in l:
            if v in graph[i]:
                break
            else:
                dfs(i)


n = int(input())
graph = [[] for _ in range(n)]
node = list(map(int, input().split()))
for i in range(n):
    if node[i] == -1:
        graph[i].append(-1)
    else:
        graph[i].append(node[i])
        graph[node[i]].append(i)
for i in range(n):
    graph[i].sort()
remove_node = int(input())
dfs(remove_node)
count = 0
for i in graph:
    if i != -2 and len(i) == 1:
        count += 1
print(count)
