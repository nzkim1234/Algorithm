from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
people = [ [] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int,stdin.readline().split())
    people[a].append(b)
    people[b].append(a)


for i in range(1, n + 1, 1):
    visit_graph = [False] * (n + 1)
    visit_graph[0] = True
    visit_graph[i] = True
    queue = deque(people[i])
    queue.append(-1)
    count = 1
    while queue:
        current_num = queue.popleft()

        if current_num == -1 and queue:
            queue.append(-1)
            count += 1
            continue
        
        if not visit_graph[current_num]:
            queue += deque(people[current_num])
            
        visit_graph[current_num] = True

        if not False in visit_graph:
            
            break
    print(count)