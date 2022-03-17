from sys import stdin

n = int(stdin.readline())

graph = []

for _ in range(n):
    graph.append(list(map(int, map(str, stdin.readline().strip()))))

