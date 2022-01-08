from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
broken_button = []

if m != 0:
    broken_button = list(map(int, stdin.readline().split()))

result = abs(100 - n)

for i in range(500000 * 2):
    num = list(map(int, str(i)))
    is_broken = False

    for j in num:
        if j in broken_button:
            is_broken = True
            break

    if not is_broken:
        result = min(result, abs(n - i) + len(num))

print(result)