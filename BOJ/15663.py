from sys import stdin

n,m = map(int, stdin.readline().split())
nums = list(sorted(map(int, stdin.readline().split())))
answer = []


def dfs(start):


for i in range(n):
    answer = [nums]
    dfs(i)