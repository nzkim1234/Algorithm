from sys import stdin

d, k = map(int, stdin.readline().split())

dp = [0] * (d + 1)

for i in range(100000):
    dp[1] = i
    for j in range(i, 100000):
        dp[2] = j
        for a in range(3, len(dp)):
            dp[a] = dp[a - 1] + dp[a - 2]
        if dp[d] == k:
            break
    if dp[d] == k:
            break

print(dp[1])
print(dp[2])