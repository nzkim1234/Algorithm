from sys import stdin

n, m = map(int, stdin.readline().split())
nums = sorted(list(map(int ,stdin.readline().split())))
answer = []


def dfs(start, size, used_list):
    if size == m:
        print(*answer)
        return

    for i in range(n):
        if not i in used_list:
            answer.append(nums[i])
            used_list.append(i)
            dfs(i + 1, size + 1, used_list)
            answer.pop()
            used_list.pop()


for i in range(n):
    answer = [nums[i]]
    dfs(i + 1, 1, [i])

