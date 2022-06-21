from lib2to3.pgen2 import grammar
from sys import stdin

n, m = map(int, stdin.readline().split())
true_num = list(map(int ,stdin.readline().split()))
graph = [[] for _ in range(m + 1)]

for _ in range(m):
    case = list(map(int, stdin.readline().split()))
    graph[case[0]] += case[1::]

print(graph)