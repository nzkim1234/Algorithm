n = int(input())
g = list(map(int, input().split()))
best_g = max(g)
for i in range(n):
    g[i] = g[i]/best_g*100
print(round(sum(g)/n, 6))
