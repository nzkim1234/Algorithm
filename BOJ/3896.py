primes = []
n = [1] * 1299710
n[0] = 0
n[1] = 0
for i in range(1299710):
    if n[i] == 1:
        primes.append(i)
        for j in range(i+i, 1299710, i):
            if n[j] != 0:
                n[j] = 0
t = int(input())
for _ in range(t):
    k = int(input())
    s = 0
    e = len(primes)-1
    while s <= e:
        m = (s+e)//2
        if primes[m] < k:
            s = m + 1
        else:
            e = m - 1
    if primes[e+1] == k:
        print(0)
    else:
        print(primes[e+1] - primes[e])
