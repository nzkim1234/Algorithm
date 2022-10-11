from sys import stdin

n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
dp = [1] * n
result = []

for i in range(1, n):
    for j in range(0, i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_len = max(dp)

for i in range(n -1, -1, -1):
    if dp[i] == max_len:
        result.append(a[i])
        max_len -= 1

print(max(dp))
print(*reversed(result))