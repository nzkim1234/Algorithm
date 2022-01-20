from sys import stdin
from collections import deque

n = int(stdin.readline())
meeting_time = []

for _ in range(n):
    meeting_time.append(list(map(int,stdin.readline().split())))

meeting_time.sort(key = lambda x: (x[1], x[0]))
result = 0
meeting_start = 0

for meeting in meeting_time:
    if meeting[0] >= meeting_start:
        meeting_start = meeting[1]
        result += 1

print(result)

