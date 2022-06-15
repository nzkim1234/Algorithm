from sys import stdin, setrecursionlimit
setrecursionlimit(int(1e9))

n = int(stdin.readline())
tree = [[] for _ in range(n + 1)]
visited_graph = [0 for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]  # [얼리 아답타 x, 얼리 아답타 o]

for _ in range(n - 1):
    u, v = map(int, stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)


def dfs(s):
    visited_graph[s] = 1
    
    for i in tree[s]:
        if visited_graph[i] == 0:
            dfs(i)
            dp[s][1] += min(dp[i][0], dp[i][1])  # 얼리 어답타인 경우 인접 노드가 뭐든 상관 없음
            dp[s][0] += dp[i][1]  # 아닐 시 인접노드는 무조건 얼리어답터여야한다
    dp[s][1] += 1


dfs(1)
print(min(dp[1][0], dp[1][1]))
