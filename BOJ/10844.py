from sys import stdin

n = int(stdin.readline())
dp = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, 101):
    for j in range(10):
        if j == 0:  # 0일때 계단수가 될 수 있는 경우는 1일때 뿐
            dp[i][j] = dp[i - 1][1]
        elif 1 <= j < 9:  # 1~8은 각각 +1, -1 한 값이 계단수
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        else:  # 9일때 계단수가 될 수 있는 경우는 8일때 뿐
            dp[i][j] = dp[i - 1][8]

print(sum(dp[n]) % 1000000000)
