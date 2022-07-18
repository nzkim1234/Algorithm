from sys import stdin
import heapq

n, k = map(int, stdin.readline().split())
graph = [1e9] * 100001
graph[n] = 0
queue = []
heapq.heappush(queue, [0, n])

while queue:
    time, current = heapq.heappop(queue)

    if current == k:
        break

    if 0 <= current * 2 <= 100000 and time < graph[current * 2]:
        graph[current * 2] = time
        heapq.heappush(queue, [time, current * 2])

    if 0 <= current + 1 <= 100000 and time < graph[current + 1]:
        graph[current + 1] = time + 1
        heapq.heappush(queue, [time + 1, current + 1])
        
    if 0 <= current - 1 <= 100000 and time < graph[current - 1]:
        graph[current - 1] = time + 1
        heapq.heappush(queue, [time + 1, current - 1])

print(graph[k])