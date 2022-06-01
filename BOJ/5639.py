from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)

nums = []

# 입력이 없을 때 까지 받아주기
while True:
    try:
        num = int(stdin.readline())
        nums.append(num)
    except:
        break


#후위 순회 계산
def order(first, end):
    if first >= end:
        return

    mid = end + 1
    
    for i in range(first + 1, end + 1):
        if nums[first] < nums[i]:
            mid = i
            break

    order(first+1, mid - 1)
    order(mid, end)
    print(nums[first])


order(0, len(nums) - 1)
