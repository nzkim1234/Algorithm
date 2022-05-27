from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    m, n, x, y = map(int ,stdin.readline().split())
    count = m * x
    print(count, n)
    if (y - count % n) <= 0:
        print(-1)
    else:
        print(count + (y - count % n))