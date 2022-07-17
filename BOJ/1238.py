from sys import stdin
import heapq

n, m, x = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
result = 0

for _ in range(m):
    start, end, length = map(int, stdin.readline().split())
    graph[start].append([end, length])


def calc(start):
    queue = []
    length_graph = [1e9] * (n + 1)
    heapq.heappush(queue, [0, start])
    length_graph[start] = 0

    while queue:
        length, current = heapq.heappop(queue)

        if length_graph[current] < length:
            continue

        for end, next_length in graph[current]:
            new_length = length + next_length

            if length_graph[end] > new_length:
                length_graph[end] = new_length
                heapq.heappush(queue, [new_length, end])

    return length_graph


for i in range(1, n + 1):
    arrive = calc(i)
    return_back = calc(x)
    result = max(result, arrive[x] + return_back[i])

print(result)