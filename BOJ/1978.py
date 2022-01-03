arr = [True] * 1001
arr[0] = False
arr[1] = False
for i in range(2, 1002):
    for j in range(2, 1002):
        if i*j < 1001:
            arr[i*j] = False
n = int(input())
num = list(map(int, input().split()))
count = 0
for i in num:
    if arr[i] is True:
        count += 1
print(count)
