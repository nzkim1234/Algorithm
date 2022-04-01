from sys import stdin

n = int(stdin.readline())
dp = [0] * (n + 1)
counseling = []

#입력 받기
for i in range(1, n + 1):
    counseling.append(list(map(int, stdin.readline().split())))

# 마지막에서부터 그 일차에 최댓값을 저장
for i in range(n - 1, -1, -1):
    if counseling[i][0] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], counseling[i][1] + dp[i + counseling[i][0]])
print(dp[0])