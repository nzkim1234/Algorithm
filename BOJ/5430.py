t = int(input())
result = []

for _ in range(t):
    p = input()
    p = p + '0'
    n = int(input())
    x = input()[1:-1].split(',')
    f = 0
    l = 0
    reverse = False
    for i in p:
        if n < 0:
            result.append('error')
            break
        if i == 'R':
            reverse = not reverse
        elif i == 'D':
            if reverse:
                l -= 1
                n -= 1
            else:
                f += 1
                n -= 1
    if n < 0:
        continue
    if n == 0:
        result.append('[]')
    else:
        if reverse:
            if l != 0:
                result.append('[' + ','.join(reversed(x[f:l])) + ']')
            else:
                result.append('[' + ','.join(reversed(x[f:])) + ']')
        else:
            if l != 0:
                result.append('[' + ','.join(x[f:l]) + ']')
            else:
                result.append('[' + ','.join(x[f:]) + ']')
for i in result:
    print(i)

