from sys import stdin

n = int(stdin.readline())

pillar = []
max_h = 0
for _ in range(n):
    l, h = map(int, stdin.readline().split())
    max_h = max(max_h, h)
    pillar.append([l, h])


pillar.sort()
stack = []
print(pillar)
for l, h in pillar:
    if not stack:
        if h > 0:
            stack.append([l, h])
    else:
        if h == max_h:
            print(stack)
            print('asdfasdf')
            break

        if stack[-1][1] < h:
            stack.append([l, h])
        
print(stack)