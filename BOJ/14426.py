n, m = map(int, input().split())
sw = []
for _ in range(n):
    sw.append(input())
sw.sort()
result = 0
for _ in range(m):
    w = input()
    s = 0
    e = len(sw) - 1
    while s <= e:
        m = (s+e)//2
        i = 0
        t = 0
        for j in w:
            if ord(j) > ord(sw[m][i]):
                s = m + 1
                t = 0
                break
            elif ord(j) < ord(sw[m][i]):
                e = m - 1
                t = 0
                break
            else:
                t = 1
            i += 1
        if t == 1:
            result += 1
            break
print(result)
