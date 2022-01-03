import sys
sys.setrecursionlimit(10**6)

r, c = map(int, input().split())
latest = 0
time = 0 
case = []
for _ in range(r):
    case.append(input().split())
melt_l = []
position = [[0, 1], [0, -1], [1, 0], [-1, 0]]
case[0][0] = 'x'
def check_x(x, y):
    for a, b in position:
        if x+a >= 0 and y+b >= 0 and x+a < r and y+b < c:
            if case[x+a][y+b] == '0':
                case[x+a][y+b] = 'x'
                check_x(x+a,y+b)
while True:
    change = 0
    for i in range(r):
        for j in range(c):
            if case[i][j] == 'x':
                case[i][j] = '0'
    check_x(0, 0)
    for i in range(r):
        for j in range(c):
            if case[i][j] == 'x':
                 for a, b in position:
                    if i+a >= 0 and j+b >= 0 and i+a < r and j+b < c:
                        if case[i+a][j+b] == '1':
                            change = 1
                            if [i+a, j+b] not in melt_l:
                                melt_l.append([i+a, j+b])
    if change == 1:
        latest = len(melt_l)
        time += 1
        for x, y in melt_l:
            case[x][y] = 'x'
        melt_l = []
    else:
        break
print(time)
print(latest)
