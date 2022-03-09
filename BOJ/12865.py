import queue
from sys import stdin

n, k = map(int, stdin.readline().split())
dp = [0] * (k + 1)
queue = []
for _ in range(n):
    w, v = map(int ,stdin.readline().split())
    queue.append([w, v])

queue.sort(reverse= True)
print(queue)