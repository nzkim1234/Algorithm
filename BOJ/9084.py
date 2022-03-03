from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    coins = list(map(int, stdin.readline().split()))
    money = int(stdin.readline())

    dp = [0] * (money + 1)
    dp[0] = 1  # 베이스

    # j 금액에서 i코인만큼 빼면 dp[j] = dp[j -i]가 성립 
    # ex) j = 4이고 i = 2일 때, dp[4] = dp[j - i] = dp[2]   즉 2원일 떄 만들어 질 수 있는 경우에 각각 + 2(i의 코인)를 하면 4원이 된다.
    # dp[2]는 1 + 1, 2 두가지 경우, dp[4]는 1 + 1 + 1 + 1(이 경우는 i = 1일때 이미 처리된 값), 1 + 1 + 2, 2 + 2이다. 뒤에 2개의 값 은 dp[2]에서 각 + 2한 값이다.
    for i in coins:
        for j in range(1, money + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    
    print(dp[money])
