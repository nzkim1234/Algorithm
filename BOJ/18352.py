# PyPy3
import heapq
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [1e9] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
q = []
heapq.heappush(q, (x, 0))
distance[x] = 0
while q:
    now, dist = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        new_dist = dist + i[1]
        if distance[i[0]] > new_dist:
            distance[i[0]] = new_dist
            heapq.heappush(q, (i[0], distance[i[0]]))
result = []
for i in range(n+1):
    if distance[i] == k:
        result.append(i)
if result:
    for i in result:
        print(i)
else:
    print(-1)
