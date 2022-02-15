from sys import stdin

n = int(stdin.readline())

dp = [1] * n
stack = list(map(int,stdin.readline().split()))

for i in range(n):
    for j in range(i):
        if stack[i] > stack[j]:
            # 앞에 상자가 더 작을 때 dp값 비교 후 갱신 
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))