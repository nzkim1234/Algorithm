from sys import stdin

while True:    
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break
    g = int(stdin.readline())
    grave = []
    for _ in range(g):
        grave.append(list(map(int,stdin.readline().split())))
    e = int(stdin.readline())
    hole = []
    for _ in range(e):
        hole.append(list(map(int,stdin.readline().split())))

    print(grave)
    print(hole)