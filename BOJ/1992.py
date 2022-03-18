from sys import stdin
from math import log2
n = int(stdin.readline())

graph = []
stack = []
for _ in range(n):
    graph.append(list(map(int, map(str, stdin.readline().strip()))))

def dfs(s_x, e_x, s_y, e_y):