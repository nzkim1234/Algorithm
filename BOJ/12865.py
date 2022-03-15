from sys import stdin

n, k = map(int, stdin.readline().split())
stuff = [[0, 0]]
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for _ in range(n):
    stuff.append(list(map(int, stdin.readline().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = stuff[i][0]  # 무게
        v = stuff[i][1]  # 가치
        # 무게보다 작을때는 이전 열에서 같은 무게의 값을 가져옴
        if j < w:
            dp[i][j] = dp[i - 1][j]
        # 자신의 무게 + j - 무게를 이전 열에서 가져옴, 이전 열에서 같은 무게의 값 중 큰값
        else:
            dp[i][j] = max(v + dp[i - 1][j - w],  dp[i - 1][j])

print(dp[n][k])
