import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    for k in adj[v]:
        if not visited[k]:
            dfs(k)


n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 0

for i in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)
    
for j in range(1, n + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
