from sys import stdin
from collections import deque

t = int(stdin.readline())

for _ in range(t):
    a, b = map(int, stdin.readline().split())
    graph = [False for _ in range(10000)]
    q = deque()
    q.append(a)
    graph[a] = " "

    while q:
        num = q.popleft()
        
        if num == b:
            print(graph[num])
            break

        next_num = 2 * num % 10000
        
        if next_num < 10000 and not bool(graph[next_num]):
            q.append(next_num)
            graph[next_num] = graph[num] + 'D'
            
        next_num = (num - 1) % 10000

        if next_num < 10000 and not graph[next_num]:
            q.append(next_num)
            graph[next_num] = graph[num] + 'S'

        next_num = (10 * num + num // 1000) % 10000

        if next_num < 10000 and not graph[next_num]:
            q.append(next_num)
            graph[next_num] = graph[num] + 'L'
        
        next_num = (num // 10 + num % 10 * 1000) % 10000

        if next_num < 10000 and not graph[next_num]:
            q.append(next_num)
            graph[next_num] = graph[num] + 'R'