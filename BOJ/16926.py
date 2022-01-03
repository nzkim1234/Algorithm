from collections import deque

n,m,r = map(int, input().split())
table = []
for _ in range(n):
    table.append(input().split())
s_r = 0
e_r = n-1
s_c = 0
e_c = m-1
c = 0
while c < min(n,m)//2:
    q = deque()
    for i in range(s_c, e_c):
        q.append(table[s_r][i])
    for i in range(s_r, e_r):
        q.append(table[i][e_c])
    for i in range(e_c, s_c, -1):
        q.append(table[e_r][i])
    for i in range(e_r, s_r, -1):
        q.append(table[i][s_c])
    if r % len(q) != 0:
        for _ in range(r % len(q)):
            q.append(q.popleft())
        for i in range(s_c, e_c):
            table[s_r][i] = q.popleft()
        for i in range(s_r, e_r):
            table[i][e_c] = q.popleft()
        for i in range(e_c, s_c, -1):
            table[e_r][i] = q.popleft()
        for i in range(e_r, s_r, -1):
            table[i][s_c] = q.popleft()
    s_r += 1
    e_r -= 1
    s_c += 1
    e_c -= 1
    c += 1
for i in range(n):
    for j in range(m):
        print(table[i][j], end = ' ')
    print()
