a, b = map(int, input().split())
l = []
c = 0

def calc(a, b, c):
    c += 1
    if a == b:
        l.append(c)
    if a * 2 <= b:
        calc(a*2, b, c)
    if a*10+1 <= b:
        calc(a*10+1, b, c)
calc(a, b, c)
if len(l) != 0:
    print(*l)
else:
    print(-1)