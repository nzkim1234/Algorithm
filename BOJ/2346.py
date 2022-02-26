from sys import stdin
from collections import deque
n = int(stdin.readline())
input = list(map(int, stdin.readline().split()))
graph = deque()

for i in range(n):
    graph.append([i + 1, input[i]])

rotate = 0
result = []
while graph:
    if rotate == 0:
        value = graph.popleft()
        result.append(value[0])
        if value[1] < 0:
            rotate = value[1] 
        else:
            rotate = value[1] - 1
    if not graph:
        break
    if rotate < 0:
        rotate += 1
        graph.appendleft(graph.pop())
    else:
        rotate -= 1
        graph.append(graph.popleft())
print(*result)