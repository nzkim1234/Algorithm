import sys
input = sys.stdin.readline

n, d = map(int, input().split())
graph = [[] for _ in range(10001)]
for _ in range(n):
    s, e, l = map(int, input().split())
    graph[s].append([l, e])
distance = [i for i in range(d+1)]

for i in range(d+1):
    if i != 0:
        distance[i] = min(distance[i], distance[i-1]+1)
    for l, e in graph[i]:
        if e <= d and distance[e] > l + distance[i]:
            distance[e] = l + distance[i]

print(distance[d])
