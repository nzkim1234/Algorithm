from sys import stdin

n, m = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))
sum_list = [0]
sums = 0

for i in nums:
    sums += i
    sum_list.append(sums)

for _ in range(m):
    s, e = map(int, stdin.readline().split())
    print(sum_list[e] - sum_list[s - 1])