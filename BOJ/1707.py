from sys import stdin
from collections import deque

t = int(stdin.readline())

for _ in range(t):
    v, e = map(int, stdin.readline().split())
    graph = [[] for _ in range(v + 1)]
    visit_graph = [False] * (v + 1)

    # 노드 추가
    for _ in range(e):
        u, a = map(int, stdin.readline().split())
        graph[u].append(a)
        graph[a].append(u)
    
    for i in range(1, v + 1):
        # 방문하지 않았다면 bfs실행
        if not visit_graph[i]:
            queue = deque([i])
            visit_graph[i] = 1
            flag = True
            
            while queue:
                current = queue.popleft()

                for j in graph[current]:
                    if not visit_graph[j]:
                        queue.append(j)
                        visit_graph[j] = -1 * visit_graph[current]  # 인접한 노드와 서로 다른 값을 가진다.
            
                    elif visit_graph[j] == visit_graph[current]:  # 인접한 노드와 서로 같은 값을 가지면 break
                        flag = False
                        break
            
                if not flag:
                    break
            
            if not flag:
                break

    if flag:
        print('YES')
    else:
        print('NO')
