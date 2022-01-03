c, r = map(int, input().split())
k = int(input())
table = [[0 for _ in range(c)] for _ in range(r)]

if k > r*c:
    print(0)
    quit()
x, y = 0, 0
position = [[1,0], [0,1], [-1,0], [0,-1]]
p_l = 0
for i in range(1, r*c+1):
    table[x][y] = i
    if i == k:
        print(y + 1, x + 1)
    if 0 <= x+ position[p_l][0] < r and 0 <= y+position[p_l][1] < c:
        if table[x+ position[p_l][0]][y+ position[p_l][1]] == 0:
            x += position[p_l][0]
            y += position[p_l][1]
        else:
            p_l += 1
            if p_l > len(position)-1:
                p_l = 0
            x += position[p_l][0]
            y += position[p_l][1]
    else:
        p_l += 1
        if p_l > len(position)-1:
            p_l = 0
        x += position[p_l][0]
        y += position[p_l][1]
