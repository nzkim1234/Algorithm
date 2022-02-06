import re
from sys import stdin

n = int(stdin.readline())

graph = list(map(int, stdin.readline().split()))
stack = []
result = []

for i in range(n):
    num = graph[i]
    
    if not stack:
        result.append(0)
        stack.append([i + 1, num])
    else:
        while stack and num > stack[-1][1]:
            stack.pop()

        if not stack:
            result.append(0)
        else:            
            result.append(stack[-1][0])

        stack.append([i + 1, num])

print(*result)