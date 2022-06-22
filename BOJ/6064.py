from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    m, n, x, y = map(int ,stdin.readline().split())
    printed = False
    k = x  # x는 고정되어야 함

    while k <= m * n:
        if (k - y) % n == 0:  # m의 조건은 항상 만족한다, 따라서 k - y % n == 0 이면 n도 만족하게 된다.
            print(k)
            printed = True
            break
        k += m 

    if not printed:
        print(-1)
        