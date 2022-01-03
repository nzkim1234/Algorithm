a = int(input())
result = []
for i in range(a):
    c = int(input())
    q = c // 25
    c = c - 25 * q
    d = c // 10
    c = c - 10 * d
    n = c // 5
    c = c - 5 * n
    p = c // 1
    r = str(q) + ' ' + str(d) + ' ' + str(n) + ' ' + str(p)
    result.append(r)
for i in range(a):
    print(result[i])
