from sys import stdin

n = int(stdin.readline())

dp = [100001 for _ in range(n + 1)]

for i in range(n + 1):
    if i * i < n + 1:
        dp[i * i] = 1

for i in range(1, n + 1):
    if dp[i] == 100001:
        for j in range(i - 1, i // 2 - 1, -1):
            dp[i] = min(dp[i], dp[j] + dp[i - j])
print(dp[n])
