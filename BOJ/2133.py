from sys import stdin

n = int(stdin.readline())
dp = [0] * (n + 1)

if n > 1:
    dp[2] = 3

    for i in range(3, n + 1, 1):
        if i % 2 == 0:  # 홀수일때는 무조건 0개 
            next_case = i - 2 
            dp[i] += dp[next_case] * dp[i - next_case]

            # dp[2] 이상부터는 특별한 경우의수가 각 2가지씩 나오게 된다 그러므로
            # 2(특별한 경우) * dp[남은칸]을 반복
            while next_case:
                next_case -= 2

                dp[i] += 2 * dp[next_case]
            
            # 특별한 경우 2개     
            dp[i] += 2

print(dp[n])

"""
ex) dp[8]
dp[2] = 3
dp[4] = 11
dp[6] = 41


계산
dp[8] = 0
dp[8] += dp[6] * dp[2]
dp[8] += 2 * dp[4]
dp[8] += 2 * dp[2]
dp[0] += 2


"""