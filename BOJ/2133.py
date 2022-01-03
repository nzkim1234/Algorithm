from sys import stdin

n = int(stdin.readline())
dp = [0] * (n + 1)

if n > 1:
    dp[2] = 3

    for i in range(3, n + 1, 1):
        if i % 2 == 0:
            next_case = i - 2
            dp[i] += dp[next_case] * dp[i - next_case]

            while next_case:
                next_case -= 2

                dp[i] += 2 * dp[next_case]
                
            dp[i] += 2

print(dp[n])