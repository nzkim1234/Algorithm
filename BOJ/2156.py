from sys import stdin

n = int(stdin.readline())
dp = [0] * n
wine = []

for i in range(n):
    wine.append(int(stdin.readline()))

dp[0] = wine[0]  # 첫번째 와인까지 마셨을 때 제일 많이 마실 수 있는 경우의 수

for i in range(1, n):
    if i == 1:  # 두번째 와인까지 마셨을때 제일 많이 마실 수 있는 경우의 수
        dp[i] = wine[0] + wine[1]
    elif i == 2:  # 세번째 와인까지 마셨을때 제일 많이 마실 수 있는 경우의 수
        dp[i] = max(wine[0] + wine[2], wine[2] + wine[1])
    else:  # i번째 와인까지 마셨을때 제일 많이 마실 수 있는 경우의 수
        dp[i] = max(wine[i] + wine[i-1] + max(dp[0 : i - 2]), wine[i] + max(dp[0: i - 1]))
    
print(max(dp))
