n, m = map(int, input().split())
dp = []
for i in range(n):
    dp.append([])
    for j in range(m):
        dp[i].append('l')
dp[1][1] = 'w'
for i in range(1, n):
    for j in range(1, m):
        