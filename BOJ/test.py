from sys import stdin

n = int(stdin.readline())

dp = [1] * (n + 1)
dp[1] = 1
dp[2] = 1

for i in range(3, n + 1):
    for x in range(i - 2, 0, -1):
        dp[i] += dp[x]

print(dp[n])