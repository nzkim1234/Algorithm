t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    floor = 0
    num = 1
    for j in range(n):
        if floor == h:
            num += 1
            floor = 0
        floor += 1
    print(str(floor) + '{0:02d}'.format(num))
