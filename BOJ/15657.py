from sys import stdin

n, m = map(int, stdin.readline().split())
nums = sorted(list(map(int ,stdin.readline().split())))
answer = []


def dfs(start, size):
    if size == m:
        print(*answer)
        return

    for i in range(start, n):
        answer.append(nums[i])
        dfs(i, size + 1)
        answer.pop()


for i in range(n):
    answer = [nums[i]]
    dfs(i, 1)
