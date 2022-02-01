from sys import stdin

n, m, b = map(int , stdin.readline().split())

graph = []
dic = { i: 0 for i in range(257)}

for _ in range(n):
    heights = list(map(int,stdin.readline().split()))
    for land in heights:
        dic[land] += 1
    graph.append(heights)

print(dic.)