from sys import stdin
from collections import deque

t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    beer = 20
    home = list(map(int, stdin.readline().split()))
    cvs = []

    for _ in range(n):
        cvs.append(list(map(int, stdin.readline().split())))

    end = list(map(int, stdin.readline().split()))
    location = cvs + [end]
    queue = deque()
    queue.append([home[0], home[1], beer])
    visit = []
    visit.append(queue[0])
    success = False

    while queue:
        x, y, beer = queue.popleft()

        if [x, y] == end:
            success = True
            break
        
        for n_x, n_y in location:
            if [n_x, n_y, 20] not in visit:
                length = abs(n_x - x) + abs(n_y - y)

                if beer * 50 >= length:
                    queue.append([n_x, n_y, 20])
                    visit.append([n_x, n_y, 20])

    if success:
        print('happy')
    else:
        print('sad')