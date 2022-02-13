from sys import stdin
from copy import deepcopy
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

base = []
while  True:
    for p_n in prime_num:
        if radius[0] % p_n == 0:
            radius[0] = radius[0] // p_n
            base.append(p_n)
            break
    if radius[0] == 1:
        break
base.sort()

for circle in radius[1::]:
    c1 = []
    c2 = deepcopy(base)
    while True:
        for p_n in prime_num:
            if circle % p_n == 0:
                circle = circle // p_n
                c1.append(p_n)
                break
        if circle == 1:
            break

    if len(c1) < len(c2):
        min_len = deepcopy(c1)
    else:
        min_len = deepcopy(c2)
    
    for i in min_len:
        if i in c1 and i in c2:
            c1.remove(i)
            c2.remove(i)
    
    if not c1:
        c1.append(1)

    if not c2:
        c2.append(1)

    mul1 = 1
    mul2 = 1
    for mul in c1:
        mul1 *= mul

    for mul in c2:
        mul2 *= mul

    result = str(mul2) + '/' + str(mul1)
    print(result)