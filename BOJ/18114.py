from sys import stdin

n, c = map(int, stdin.readline().split())

graph = list(map(int, stdin.readline().split()))

start = end = 0
result = 0
count = 0
while start <= end:
    if count < c:
        count += graph[end]
        end += 1
        
    elif count == c:
        result = 1
        break
    else:
        start += 1
        count -= graph[start]

print(result)