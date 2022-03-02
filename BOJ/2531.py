from sys import stdin
from collections import deque

n, d, k, c = map(int, stdin.readline().split())
line = []

for _ in range(n):
    line.append(int(stdin.readline()))

start = 0
result = 0

while True:
    end = start + k
    can_eat = []
    count = 0

    if start > n - 1:
        break
    
    if end > n - 1:
        end = end % n

    for i in range(k):
        index = start + i

        if index > n - 1:
            break
        
        can_eat.append(line[start + i])
        count += 1
    
    if count < k:
        can_eat += line[:end]
    
    if not c in can_eat:
        can_eat.append(c)

    result = max(result, len(set(can_eat)))
    start += 1

print(result)
