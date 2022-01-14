from operator import le
import queue
from sys import stdin
import heapq

n = int(stdin.readline())
m = int(stdin.readline())

graph = [[] for _ in range(n)]
least_cost = [1e9] * n

for _ in range(m):
    start, end, cost = map(int, stdin.readline().split())
    graph[start - 1].append([end - 1, cost])   

start, end = map(int, stdin.readline().split())
least_cost[start - 1] = 0

queue = []
heapq.heappush(queue, [0, start -1])

while queue:
    s_cost, s_node = heapq.heappop(queue)
    if least_cost[s_node] < s_cost:
        continue
    for node, cost in graph[s_node]:
        if s_cost + cost < least_cost[node]:
            least_cost[node] = s_cost + cost
            heapq.heappush(queue, [least_cost[node], node])

        

print(least_cost[end - 1])