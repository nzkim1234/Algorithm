from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    nums = []

    for _ in range(n):
        nums.append(stdin.readline().strip())
    
    nums.sort()
    able = True

    for i in range(n-1):
        if(nums[i+1].startswith(nums[i])):
            able = False
            break
        
    if able:
        print('YES')
    else:
        print('NO')