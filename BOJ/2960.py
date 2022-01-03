n, k = map(int, input().split())
n_l = [True for _ in range(n+1)]
n_l[0] = False
n_l[1] = False
result = 0
for i in range(n+1):
    if n_l[i] == True:
        for j in range(i, n+1, i):
            if n_l[j] == True:
                k -= 1
                n_l[j] = False
                if k == 0:
                    result = j
                    break
    if k == 0:
        break
print(result)
