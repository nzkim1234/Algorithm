from re import L
from sys import stdin
from math import ceil

n, h = map(int ,stdin.readline().split())

cave = []

for i in range(n):
    if i % 2 ==0:
        cave.append(int(stdin.readline()))
    else:
        cave.append(h - int(stdin.readline()))
print(cave)
cave.sort()
print(cave)
for i in range(h):
    if i < ceil(h/2):
        i += 0.5
    else:
        i = h - 1 - i + 0.5
    print()
    print(i)

    start = 0
    end = len(cave) - 1

    while start < end:
        mid = (start + end) // 2

        if cave[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
        
    print(mid)
