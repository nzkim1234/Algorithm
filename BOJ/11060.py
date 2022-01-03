n = int(input())
a = list(map(int, input().split()))
dp = [1001] * n
dp[0] = 0
for i in range(n):
    r = a[i]
    for j in range(r+1):
        if i+j < n:
            dp[i+j] = min(dp[i]+1, dp[i+j])
print(dp[-1] if max(dp) != 1001 else -1)
