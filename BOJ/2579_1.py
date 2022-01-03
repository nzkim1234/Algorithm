from sys import stdin

n = int(stdin.readline())
stairs = [int(input()) for _ in range(n)]
dp = [[ ] for _ in range(n)]

if n < 2:  # 계단의 수가 1개 이하면 그 계단의 값을 출력
    print(stairs[0])

else:
    # dp[0], dp[1]은 최초값
    dp[0] = [[stairs[0], 1]]
    dp[1] = [[stairs[0]+ stairs[1], 2], [stairs[1], 1]]

    # 2번째 계단부터 n번째 계단까지 각 계단별 최댓값 구하기
    for i in range(2, n):
        current_stair = stairs[i]
        max_sum = 0

        # 한 칸 아래의 계단에서 올라올때의 최댓값 구하기
        for sum, in_row in dp[i-1]:  
            if in_row != 2:
                max_sum = max(max_sum, stairs[i] + sum)

        dp[i].append([max_sum, 2])

        # 두 칸 아래의 계단에서 올라올때의 최댓값 구하기
        dp[i].append([max(dp[i-2])[0] + stairs[i], 1])
        
    print(max(dp[-1])[0])