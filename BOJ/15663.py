from sys import stdin

n,m = map(int, stdin.readline().split())
nums = list(sorted(map(int, stdin.readline().split())))
visited_list = [False] * n
answer = []


def dfs():
    if len(answer) == m:
        print(*answer)
    
    else:
        previous_num = 0

        for i in range(n):
            if not visited_list[i] and previous_num != nums[i]:
                visited_list[i] = True
                answer.append(nums[i])
                previous_num = nums[i]
                dfs()
                visited_list[i] = False
                answer.pop()


dfs()
