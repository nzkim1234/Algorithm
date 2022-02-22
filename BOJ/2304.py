from sys import stdin

n = int(stdin.readline())
graph = [0] * 1000
max_x = 0
max_y = 0
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    graph[x - 1] = y

index = graph.index(max_y)
check = 0
result = 0

for i in range(index):
    check = max(check, graph[i])
    result += check
print(result)
check = 0

for i in range(max_x, index, -1):
    check = max(check, graph[i])
    result += check

print(result + max_y)