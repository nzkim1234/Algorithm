from sys import stdin

n = int(stdin.readline())

radius = list(map(int, stdin.readline().split()))
result = []

num = [True for _ in range(1001)]
prime_num = []

for i in range(2, 1001):
    if num[i]:
        for j in range(i + i, 1001, i):
            num[j] = False
        prime_num.append(i)

c2 = []
while  True:
    for p_n in prime_num:
        if radius[0] % p_n == 0:
            radius[0] = radius[0] // p_n
            c2.append(p_n)
            break
    if radius[0] == 1:
        break
c2.sort()

for circle in radius[1::]:
    c1 = []
    new_c2 = c2    
    while  True:
        for p_n in prime_num:
            if circle % p_n == 0:
                circle = circle // p_n
                c1.append(p_n)
                break
        if circle == 1:
            break
    c1.sort()

    if len(c2) < len(c1):
        min_c = c2
    else:
        min_c = c1
    
    for i in min_c:
        if (i in c1) and (i in new_c2):
            c1.remove(c1.index(i))
            new_c2.remove(new_c2.index(i))
    print(c1, c2)
    print()
