import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    dp = [arr[0]]
    for i in range(1, n):
        dp.append(max(dp[i-1] + arr[i], arr[i]))
    print(max(dp))

'''
import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    for i in range(1, n):
        arr[i] = max(arr[i-1] + arr[i], arr[i])
    print(max(arr))

--------------------------------------------------
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    arr = [int(input()) for _ in range(n)]
    for i in range(1, n):
        arr[i] = max(arr[i-1] + arr[i], arr[i])
    print(max(arr))
'''
