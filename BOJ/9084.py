from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    coins = list(map(int, stdin.readline().split()))
    money = int(stdin.readline())
    dp = [0] * (money + 1)
    dp[0] = 1
    for i in coins:
        for j in range(1, money + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    print(dp[money])