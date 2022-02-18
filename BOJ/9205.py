from sys import stdin

t = int(stdin.readline())
n = int(stdin.readline())

graph = [['_' for _ in range(65536)] for _ in range(655336)]
print(graph[0])
home = list(map(int, stdin.readline().split()))